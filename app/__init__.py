#===========================================================
# PROJECT NAME HERE
# By YOUR NAME HERE
#===========================================================

from flask import Flask, request, session, render_template, flash, redirect, send_file, make_response
from werkzeug.security import generate_password_hash, check_password_hash, secure_filename
from dotenv import load_dotenv
from os import getenv
from io import BytesIO
import html
from app.helpers import *


# Create the app
app = Flask(__name__)


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
    link = request.form.get("link")
    image = request.form.get("image")
    

    # Get the file selected via the form
    logo = request.files.get('logo', None)
    if not logo or logo.filename == '':
        flash("There was a problem uploading the image", "error")
        return redirect("/")

    # Sanitise filename and make it unique
    filename = secure_filename(logo.filename)
    random_prefix = uuid.uuid4().hex[:12]
    unique_filename = f"{random_prefix}_{filename}"

    # Get the path of the upload folder
    filepath = os.path.join(UPLOAD_FOLDER, unique_filename)

    # Save file to disk
    logo.save(filepath)

    # Add the form data and the upload filename to the DB
    with connect_db() as db:
        sql = "INSERT INTO clubs (name, logo_filename) VALUES (?, ?)"
        params = (name, unique_filename)
        db.execute(sql, params)

        flash(f"Club '{name}' added", "success")
        return redirect("/things")



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

