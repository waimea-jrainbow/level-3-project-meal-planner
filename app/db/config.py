#============================================================================
# Database schema and seed data configuration
#============================================================================


#----------------------------------------------------------------------------
# Table definitions
#----------------------------------------------------------------------------
# Define your tables with a name, a schema and optional seed/sample data,
# using this format, and then add the tables to the Table Registry below:
#
# class TableName:
#     NAME      = "name"
#     SCHEMA    = "CREATE TABLE name (...)"
#     SEED_DATA = "INSERT INTO name (...)" or None
#----------------------------------------------------------------------------

class UserTable:

    NAME = "users"

    SCHEMA = """
        CREATE TABLE `users`(
        `id` INTEGER PRIMARY KEY AUTOINCREMENT,
        `email` TEXT NOT NULL,
        `password_hash` TEXT NOT NULL,
        `display_name` TEXT NOT NULL
    )
    """
    #TODO fill tables with test data
    SEED_DATA = """
        INSERT INTO users ("email", "password_hash", "display_name")
        VALUES
            ("goober@gmail.com", "1234", "goober"),
            
    """
    
    
class HouseholdTable:
    
    NAME = "households"

    SCHEMA = """
        CREATE TABLE `households`(
        `id` INTEGER PRIMARY KEY AUTOINCREMENT,
        `name` TEXT NOT NULL,
        `join_code` INTEGER NOT NULL UNIQUE,
        
        `created_by` TEXT NOT NULL, 
        
        FOREIGN KEY(created_by) REFERENCES users(id)
    )
    """
    
    SEED_DATA = """
        INSERT INTO users ("name", "join_code", "created_by")
        VALUES
            ("Goobers house", "goobers join code", "1"),
    """


class HouseholdMembersTable:
    
    NAME = "householdMembers"
    
    SCHEMA = """
        CREATE TABLE `household_members`(
        `household_id` INTEGER,
        `user_id` INTEGER NOT NULL ,
        `role` TEXT NOT NULL,
        
        PRIMARY KEY(household_id, user_id)
        
        FOREIGN KEY(household_id) REFERENCES households(id),
        FOREIGN KEY(user_id) REFERENCES users(id)        
    )
    """
    
    SEED_DATA = """
        INSERT INTO users ("household_id", "user_id", "role")
        VALUES
            ("1","1","owner"),
    """
    
    
class RecipeTable:
    
    NAME = "recipes"
    
    SCHEMA = """
        CREATE TABLE `recipes`(
        `id` INTEGER PRIMARY KEY AUTOINCREMENT,
        `household_id` INTEGER NOT NULL,
        `title` TEXT NOT NULL,
        `url` TEXT,
        `image_path` TEXT,
        `notes` TEXT,
        'ingredients' TEXT,
        'method' TEXT
        FOREIGN KEY(household_id) REFERENCES households(id)
    )
    """
    
    
    SEED_DATA = """
        INSERT INTO users ("title", "url","image_path", "notes", "ingredients", "method")
        VALUES
            ("goober food", "goobermeals.com", "images/goobermeal.png", "notes for noting", "goober meat", "cook goober meat"
    """
    
    
class MealPlanTable:
    
    NAME = "mealPlan"

    SCHEMA = """
        CREATE TABLE `meal_plan`(
            `family_id` INTEGER,
            `date` DATETIME,
            `meal_type` TEXT,
            `recipe_id` INTEGER NOT NULL,
            
            PRIMARY KEY(family_id, date, meal_type)
            
            FOREIGN KEY(household_id) REFERENCES households(id)
            FOREIGN KEY(recipe_id) REFERENCES recipes(id)

    )
    """
    
    SEED_DATA = """
        INSERT INTO users ("date", "meal_type", "recipe_id")
        VALUES
            ("1/1/1111", "breakfast", "1"),
    """


#----------------------------------------------------------------------------
# Table registry
#----------------------------------------------------------------------------
# Register all of your tables by adding them to the TABLES list here:
#
# TABLES = [
#     Table1Name,
#     Table2Name,
#     etc.
# ]
#
# Note: The table order is important - Create the tables that have
# foreign keys *after* the tables they link to have been created
#----------------------------------------------------------------------------

TABLES = [
    UserTable,
    HouseholdTable,
    HouseholdMembersTable,
    RecipeTable,
    MealPlanTable
]

