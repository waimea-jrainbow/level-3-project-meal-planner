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
# Meal plan page route - Show all the meal plan
#-----------------------------------------------------------
@app.get("/recipes")
def show_recipes():
    with connect_db() as client:
        # Get all the things from the DB
        sql = "SELECT * FROM recipes ORDER BY title ASC"
        params = []
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
@app.get("/form/add/recipe")
def add_a_recipe_form():
   return render_template("pages/add_recipe.jinja")


#-----------------------------------------------------------
# Route for adding a recipe, using data posted from a form
#-----------------------------------------------------------
@app.post("/add/recipe")
def add_a_recipe():
    # Get the data from the form
    title  = request.form.get("title")
    url = request.form.get("link")
    meal_type = request.form.get("meal_type")
    

    # Get the file selected via the form
    image = request.files.get('image', None)
    if not image or image.filename == '':
        flash("There was a problem uploading the image", "error")
        return redirect("/form/add/recipe")

    # Sanitise filename and make it unique
    filename = secure_filename(image.filename)
    random_prefix = uuid.uuid4().hex[:12]
    unique_filename = f"{random_prefix}_{filename}"

    # Get the path of the upload folder
    filepath = os.path.join(UPLOAD_FOLDER, unique_filename)

    # Save file to disk
    image.save(filepath)

    # Add the form data and the upload filename to the DB
    with connect_db() as db:
        sql = "INSERT INTO recipes (title, url, meal_type, image_path) VALUES (?, ?, ?, ?)"
        params = (title,url, meal_type, unique_filename)
        db.execute(sql, params)
# TODO make household_id so recipe upload works
        flash(f"Club '{title}' added", "success")
        return redirect("/")

#-----------------------------------------------------------
# Add new user page
#-----------------------------------------------------------
@app.get("/form/add/user")
def add_a_user_form():
   return render_template("pages/add_user.jinja")


#-----------------------------------------------------------
# Route for adding a user, using data posted from a form
#-----------------------------------------------------------
@app.post("/add/user")
def add_a_user():
    # Get the data from the form
    email  = request.form.get("email")
    password = request.form.get("password")
    display_name = request.form.get("meal_type")
    

    # Get the file selected via the form
    image = request.files.get('image', None)
    if not image or image.filename == '':
        flash("There was a problem uploading the image", "error")
        return redirect("/form/add/recipe")

    # Sanitise filename and make it unique
    filename = secure_filename(image.filename)
    random_prefix = uuid.uuid4().hex[:12]
    unique_filename = f"{random_prefix}_{filename}"

    # Get the path of the upload folder
    filepath = os.path.join(UPLOAD_FOLDER, unique_filename)

    # Save file to disk
    image.save(filepath)

    # Add the form data and the upload filename to the DB
    with connect_db() as db:
        sql = "INSERT INTO recipes (title, url, meal_type, image_path) VALUES (?, ?, ?, ?)"
        params = (title,url, meal_type, unique_filename)
        db.execute(sql, params)
# TODO make household_id so recipe upload works
        flash(f"Club '{title}' added", "success")
        return redirect("/")

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

