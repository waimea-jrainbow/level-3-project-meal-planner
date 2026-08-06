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
        `id` INTEGER NOT NULL AUTOINCREMENT PRIMARY KEY,
        `email` TEXT NOT NULL,
        `password_hash` TEXT NOT NULL,
        `display_name` TEXT NOT NULL
    )
    """
    #TODO fill tables with test data
    SEED_DATA = """
        INSERT INTO users ("email", "password_hash", "display_name")
        VALUES
            ("Welcome!",      1, "This is a demo application using Flask, Jinja and SQLite."),
            ("Shopping List", 0, "Milk\nBread\nEggs\nCheese"),
            ("Meeting Notes", 0, "Discussed project timeline.\n\nAction items:\n- Review design\n- Update docs"),
            ("Recipe: Pasta", 0, "Ingredients:\n- 500g pasta\n- Tomato sauce\n- Garlic\n\nCook pasta, add sauce, enjoy!"),
            ("Important!",    1, "Remember to backup your database regularly.")
    """
    
    
class HouseholdTable:
    
    NAME = "households"

    SCHEMA = """
        CREATE TABLE `households`(
        `id` INTEGER NOT NULL AUTOINCREMENT PRIMARY KEY,
        `name` TEXT NOT NULL,
        `join_code` INTEGER NOT NULL UNIQUE,
        
        `created_by` TEXT NOT NULL 
        
        FOREIGN KEY(created_by) REFERENCES users(id)
    )
    """


class HouseholdMembersTable:
    
    NAME = "householdMembers"
    
    SCHEMA = """
        CREATE TABLE `household_members`(
        'household_id` INTEGER NOT NULL PRIMARY KEY,
        `user_id` INTEGER NOT NULL PRIMARY KEY,
        `role` TEXT NOT NULL,
        
        FOREIGN KEY(household_id) REFERENCES households(id)
        FOREIGN KEY(user_id) REFERENCES users(id)        
    )
    """
class RecipeTable:
    
    NAME = "recipes"
    
    SCHEMA = """
        CREATE TABLE `recipes`(
        `id` INTEGER NOT NULL AUTOINCREMENT PRIMARY KEY,
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
    
    
    
class MealPlanTable:
    
    NAME = "mealPlan"

    SCHEMA = """
        CREATE TABLE `meal_plan`(
            `family_id` INTEGER NOT NULL PRIMARY KEY,
            `date` DATETIME NOT NULL PRIMARY KEY,
            `meal_type` TEXT NOT NULL PRIMARY KEY,
            `recipe_id` INTEGER NOT NULL,
            
            FOREIGN KEY(household_id) REFERENCES households(id)
            FOREIGN KEY(recipe_id) REFERENCES recipes(id)

    )
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

