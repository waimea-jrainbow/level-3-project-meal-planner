#===========================================================
# PROJECT NAME HERE
# By YOUR NAME HERE
#===========================================================

from flask import Flask, request, session, render_template, flash, redirect, send_file, make_response, abort
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
from io import BytesIO
import html, os, uuid
from app.helpers import *


# Create the app
app = Flask(__name__)

UPLOAD_FOLDER = os.path.join('app', 'static', 'uploads')


#===========================================================
# App Routes Handlers
#===========================================================

#-----------------------------------------------------------
# Home page 
#-----------------------------------------------------------
@app.get("/")
def homepage():
   return render_template("pages/home_page.jinja")

#-----------------------------------------------------------
# recipes page route - show all household recipes
#-----------------------------------------------------------
@app.get("/recipes")
@login_required
def show_recipes():
    with connect_db() as client:
        # Get all the things from the DB
        sql = "SELECT * FROM recipes WHERE household_id=? ORDER BY title ASC "
        params = [session["user"]["household_id"]]
        result = client.execute(sql, params)
        recipes = result.fetchall()

        # And show them on the page
        return render_template("pages/recipes.jinja", recipes=recipes)


#-----------------------------------------------------------
# Recipe page route - Show details of a single recipe
#-----------------------------------------------------------
@app.get("/recipe/<int:id>")
def show_one_recipe(id):
    with connect_db() as client:
        # Get the thing details from the DB
        sql = "SELECT * FROM recipes WHERE id=?"
        params = [id]
        result = client.execute(sql, params)

        recipe = result.fetchone()
        
        # Did we get a result?
        if recipe:
            # yes, so show it on the page
            return render_template("pages/recipe.jinja", recipe=recipe)

        else:
            # No, so show error
            abort(404)


#-----------------------------------------------------------
# Add new recipe page
#-----------------------------------------------------------
@app.get("/recipe/new")
@login_required
def add_a_recipe_form():
   return render_template("pages/add_recipe.jinja")


#-----------------------------------------------------------
# Route for adding a recipe, using data posted from a form
#-----------------------------------------------------------
@app.post("/recipe")
@login_required
def add_a_recipe():

    # Get the data from the form
    title = request.form.get("title")
    url = request.form.get("link")
    meal_type = request.form.get("meal_type")

    # Get the currently logged-in user
    user_id = session["user"]["id"]

    with connect_db() as db:

        # Find the household the user belongs to
        sql = """
            SELECT household_id
            FROM household_members
            WHERE user_id=?
        """
        params = (user_id,)
        result = db.execute(sql, params)

        household = result.fetchone()

        if not household:
            flash("You need to join or create a household first", "error")
            return redirect("/household")

        household_id = household["household_id"]

        # Get the file selected via the form
        image = request.files.get("image", None)

        if not image or image.filename == "":
            flash("There was a problem uploading the image", "error")
            return redirect("/recipe/new")

        # Sanitise filename and make it unique
        filename = secure_filename(image.filename)
        random_prefix = uuid.uuid4().hex[:12]
        unique_filename = f"{random_prefix}_{filename}"

        # Get the path of the upload folder
        filepath = os.path.join(UPLOAD_FOLDER, unique_filename)

        # Save file to disk
        image.save(filepath)

        # Add recipe to the user's household
        sql = """
            INSERT INTO recipes (household_id, title, url, meal_type, image_path)
            VALUES (?, ?, ?, ?, ?)
        """
        params = (household_id, title, url, meal_type, unique_filename)
        db.execute(sql, params)

        flash(f"Recipe '{title}' added", "success")
        return redirect("/")

#-----------------------------------------------------------
# Add new user page
#-----------------------------------------------------------
@app.get("/user/new")
def add_a_user_form():
   return render_template("pages/add_user.jinja")


#-----------------------------------------------------------
# Route for adding a user, using data posted from a form
#-----------------------------------------------------------
@app.post("/user")
def add_a_user():
    # Get the data from the form
    email  = request.form.get("email")
    display_name = request.form.get("display_name")
    password = request.form.get('password', '').strip()

    with connect_db() as db:
        sql = "SELECT id FROM users WHERE email=?"
        params = (email,)
        user = db.execute(sql, params).fetchone()

        if user:
            flash(f"An account using the email address '{email}' already exists", "error")
            return redirect("/form/add/user")

        pass_hash = generate_password_hash(password)

        sql = """
            INSERT INTO users (email, display_name, password_hash)
            VALUES (?, ?, ?)
        """
        params = (email, display_name, pass_hash)
        db.execute(sql, params)

        flash("Account created. Please login", "success")
        return redirect("/login")
    
    
#-----------------------------------------------------------
# User login page
#-----------------------------------------------------------
@app.get("/login")
def login_form():
   return render_template("pages/login.jinja")

#-----------------------------------------------------------
# Route for logging in as a user, using data posted from a form
#-----------------------------------------------------------
@app.post("/login")
def login_as_user():
    email = request.form.get("email")
    password = request.form.get("password", "").strip()

    with connect_db() as db:
        sql = """
            SELECT users.id, users.email, users.display_name, users.password_hash,
                households.id AS household_id,
                households.name AS household_name
            FROM users
            LEFT JOIN household_members
                ON users.id = household_members.user_id
            LEFT JOIN households
                ON household_members.household_id = households.id
            WHERE users.email=?
"""
        params = (email,)
        user = db.execute(sql, params).fetchone()

        if not user:
            flash("Email or password incorrect", "error")
            return redirect("/login")

        if not check_password_hash(user["password_hash"], password):
            flash("Email or password incorrect", "error")
            return redirect("/login")

        else:
            session["logged_in"] = True
            session["user"] = {
            "id": user["id"],
            "display_name": user["display_name"],
            "email": user["email"],
            "household_id": user["household_id"],
            "household_name": user["household_name"]
            
            }

            flash("Successfully logged in", "success")
            return redirect("/")    
        



#-----------------------------------------------------------
# Route for logging out
#-----------------------------------------------------------       
@app.get("/logout")
@login_required
def logout_user():
    session.clear()
    flash(f"You have been logged out", "success")
    return redirect("/") 


#-----------------------------------------------------------
# household creation and joining page
#-----------------------------------------------------------
@app.get("/household")
@login_required
def household_forms():
   return render_template("pages/household_join&create.jinja")

#-----------------------------------------------------------
# Route for adding a household, using data posted from a form
#-----------------------------------------------------------
@app.post("/household")
@login_required
def add_a_household():
    # Get the data from the form
    name  = request.form.get("name")
    
    if not name:
        flash("Please enter a household name", "error")
        return redirect("/household")
    
    created_by = session["user"]["id"]
    
    with connect_db() as db:
        while True:
            join_code = str(uuid.uuid4().int)[:6]
            
            sql = """
                SELECT id FROM households WHERE join_code=?
            """
            params = (join_code,)
            existing = db.execute(sql, params).fetchone()

            if not existing:
                break

    with connect_db() as db:
        sql = """
            INSERT INTO households (name, join_code, created_by)
            VALUES (?, ?, ?)
        """
        params = (name, join_code, created_by)
        household = db.execute(sql, params)

        household_id = household.lastrowid

        sql = """
            INSERT INTO household_members (household_id, user_id, role)
            VALUES (?, ?, ?)
        """
        params = (household_id, created_by, "owner")
        db.execute(sql, params)

        session["user"]["household_id"] = household_id
        session["user"]["household_name"] = name

        flash(f"Household {name} created", "success")
        return redirect("/")


#-----------------------------------------------------------
# Route for joining a household
#-----------------------------------------------------------

@app.post("/household/join")
@login_required
def join_a_household():

    join_code = request.form.get("join_code", "").strip()

    user_id = session["user"]["id"]

    if not join_code:
        flash("Please enter a join code", "error")
        return redirect("/household")

    with connect_db() as db:

        sql = """
            SELECT
                id,
                name,
                join_code,
                created_by
            FROM households
            WHERE join_code=?
        """

        params = (join_code,)

        result = db.execute(sql, params)
        household = result.fetchone()

        # Check if the household exists
        if not household:
            flash("Invalid join code", "error")
            return redirect("/household")


        sql = """
            INSERT INTO household_members
                (household_id, user_id, role)
            VALUES
                (?, ?, ?)
        """

        params = (household["id"], user_id, "member")

        db.execute(sql, params)


        session["user"]["household_id"] = household["id"]
        session["user"]["household_name"] = household["name"]

        flash(f"You joined {household['name']}", "success")

        return redirect("/household/manage")


#-----------------------------------------------------------
# Manage household - open household dashboard
#-----------------------------------------------------------

@app.get("/household/manage")
@login_required
def household_dashboard():
    
    household_id = session["user"]["household_id"]

    # User isn't currently in a household
    if not household_id:
        flash("You are not currently in a household", "error")
        return redirect("/household")
    
    
    with connect_db() as db:

        sql = """
            SELECT
                id,
                name,
                join_code,
                created_by
            FROM households
            WHERE id=?
        """

        params = (session["user"]["household_id"],)

        result = db.execute(sql, params)
        household = result.fetchone()
        
        
        # Get household members
        sql = """
            SELECT
                users.id,
                users.display_name,
                users.email,
                household_members.role
            FROM household_members
            JOIN users
                ON household_members.user_id = users.id
            WHERE household_members.household_id=?
        """

        params = (session["user"]["household_id"],)

        result = db.execute(sql, params)
        members = result.fetchall()

        is_owner = household["created_by"] == session["user"]["id"]

        return render_template(
            "pages/manage_household.jinja",
            household=household,
            members=members,
            is_owner=is_owner
        ) 
 

#-----------------------------------------------------------
# Route to remove a user from a household as owner
#-----------------------------------------------------------      
@app.post("/household/remove_member/<int:user_id>")
@login_required
def remove_household_member(user_id):

    with connect_db() as db:

        sql = """
            SELECT created_by
            FROM households
            WHERE id=?
        """

        params = (session["user"]["household_id"],)

        result = db.execute(sql, params)
        household = result.fetchone()

        if household["created_by"] != session["user"]["id"]:
            flash("Only the household owner can remove members", "error")
            return redirect("/household/manage")

        # Don't allow owner to remove themselves
        if user_id == session["user"]["id"]:
            flash("You cannot remove yourself", "error")
            return redirect("/household/manage")

        # Remove the user from the household
        sql = """
            DELETE FROM household_members
            WHERE household_id=? AND user_id=?
        """

        params = (session["user"]["household_id"], user_id)

        db.execute(sql, params)

        flash("Member removed", "success")
        return redirect("/household/manage")

    
#-----------------------------------------------------------
# meal plan - view full meal plan 
#-----------------------------------------------------------

@app.get("/meal_plan")
@login_required
def show_meal_plan():
    with connect_db() as db:

        sql = """
            SELECT
                meal_plan.date,
                meal_plan.meal_type,
                recipes.id AS recipe_id,
                recipes.title AS recipe_title
            FROM meal_plan
            JOIN recipes
                ON meal_plan.recipe_id = recipes.id
            WHERE meal_plan.household_id=?
            ORDER BY
                meal_plan.date ASC,
                CASE meal_plan.meal_type
                    WHEN 'breakfast' THEN 1
                    WHEN 'lunch' THEN 2
                    WHEN 'dinner' THEN 3
                    ELSE 4
                END
        """

        params = (session["user"]["household_id"],)

        result = db.execute(sql, params)
        meal_plan = result.fetchall()

        return render_template(
            "pages/meal_plan.jinja",
            meal_plan=meal_plan
        )

#-----------------------------------------------------------
# Route for transferring ownership of a household
#-----------------------------------------------------------
@app.post("/household/transfer_owner/<int:user_id>")
@login_required
def transfer_owner_household(user_id):

    current_user_id = session["user"]["id"]
    household_id = session["user"]["household_id"]

    if not household_id:
        flash("You are not currently in a household", "error")
        return redirect("/household")

    with connect_db() as db:

        # Check whether the user is the household owner
        sql = """
            SELECT created_by
            FROM households
            WHERE id=?
        """

        params = (household_id,)

        result = db.execute(sql, params)
        household = result.fetchone()

        if not household:
            flash("Household not found", "error")
            return redirect("/household")

        if household["created_by"] != current_user_id:
            flash("You must be the owner to transfer ownership", "error")
            return redirect("/household/manage")

        # Make new user the owner of the household
        sql = """
            UPDATE households
            SET created_by=?
            WHERE id=?
        """

        params = (user_id, household_id)

        db.execute(sql, params)

        # Make old owner a member
        sql = """
            UPDATE household_members
            SET role=?
            WHERE household_id=? AND user_id=?
        """

        params = ("member", household_id, current_user_id)

        db.execute(sql, params)

        # Make new user an owner
        sql = """
            UPDATE household_members
            SET role=?
            WHERE household_id=? AND user_id=?
        """

        params = ("owner", household_id, user_id)

        db.execute(sql, params)

        flash("Ownership transferred successfully", "success")

        return redirect("/household/manage")
     
        
#-----------------------------------------------------------
# Route for leaving a household
#-----------------------------------------------------------
@app.post("/household/leave")
@login_required
def leave_household():

    user_id = session["user"]["id"]
    household_id = session["user"]["household_id"]

    if not household_id:
        flash("You are not currently in a household", "error")
        return redirect("/household")

    with connect_db() as db:

        # Check whether the user is the household owner
        sql = """
            SELECT created_by
            FROM households
            WHERE id=?
        """

        result = db.execute(sql, (household_id,))
        household = result.fetchone()

        if not household:
            flash("Household not found", "error")
            return redirect("/household")

        # Owner cannot leave
        if household["created_by"] == user_id:
            flash("The household owner cannot leave the household", "error")
            return redirect("/household/manage")

        # Remove the current user from the household
        sql = """
            DELETE FROM household_members
            WHERE household_id=? AND user_id=?
        """

        db.execute(sql, (household_id, user_id))

        # Clear household information from the session
        session["user"]["household_id"] = None
        session["user"]["household_name"] = None

        flash("You have left the household", "success")

        return redirect("/household")

        
#===========================================================
# Configure the app
#===========================================================
load_dotenv()
app.config.from_prefixed_env()
init_logging(app)
init_text_filters(app)
init_date_filters(app)
init_error_handlers(app)
init_database()
register_commands(app)

