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

    SEED_DATA = """
        INSERT INTO users ("email", "password_hash", "display_name")
        VALUES
            ("goober@gmail.com", "scrypt:32768:8:1$n7eJTucLbaGmUpAM$c1776374a8d456a6eaf61bccc08db5e1fcc4ff3b3983d364c45ab13074255eeae0a393afb11f99a9fe63fb1d980992ace17a72ba70324523b11e92e36cbe4252", "goober");
    """


class HouseholdTable:

    NAME = "households"

    SCHEMA = """
        CREATE TABLE `households`(
        `id` INTEGER PRIMARY KEY AUTOINCREMENT,
        `name` TEXT NOT NULL,
        `join_code` TEXT NOT NULL UNIQUE,
        `created_by` INTEGER NOT NULL,
        
        FOREIGN KEY(created_by) REFERENCES users(id)
    )
    """

    SEED_DATA = """
        INSERT INTO households ("name", "join_code", "created_by")
        VALUES
            ("Goobers house", 123456, 1);
    """


class HouseholdMembersTable:

    NAME = "household_members"

    SCHEMA = """
        CREATE TABLE `household_members`(
        `household_id` INTEGER,
        `user_id` INTEGER NOT NULL,
        `role` TEXT NOT NULL,

        PRIMARY KEY(household_id, user_id),

        FOREIGN KEY(household_id) REFERENCES households(id),
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """

    SEED_DATA = """
        INSERT INTO household_members ("household_id", "user_id", "role")
        VALUES
            (1, 1, "owner");
    """


class RecipeTable:

    NAME = "recipes"
# TODO add household_id NOT NULL back after basic testing once households exist
    SCHEMA = """
        CREATE TABLE `recipes`(
        `id` INTEGER PRIMARY KEY AUTOINCREMENT,
        `household_id` INTEGER , 
        `title` TEXT NOT NULL,
        `url` TEXT,
        `meal_type` TEXT,
        `image_path` TEXT,
        `notes` TEXT,
        `ingredients` TEXT,
        `method` TEXT,

        FOREIGN KEY(household_id) REFERENCES households(id)
    )
    """

    SEED_DATA = """
        INSERT INTO recipes (
            "household_id",
            "title",
            "url",
            "meal_type",
            "image_path",
            "notes",
            "ingredients",
            "method"
        )
        VALUES
            (
                1,
                "Goober Food",
                "https://goobermeals.com",
                "any",
                "/static/uploads/goobermeal.png",
                "Notes for noting",
                "Goober meat",
                "Cook goober meat"
            );
    """


class MealPlanTable:

    NAME = "meal_plan"

    SCHEMA = """
        CREATE TABLE `meal_plan`(
            `family_id` INTEGER,
            `date` DATETIME,
            `meal_type` TEXT,
            `recipe_id` INTEGER NOT NULL,

            PRIMARY KEY(family_id, date, meal_type),

            FOREIGN KEY(family_id) REFERENCES households(id),
            FOREIGN KEY(recipe_id) REFERENCES recipes(id)
        )
    """

    SEED_DATA = """
        INSERT INTO meal_plan ("family_id", "date", "meal_type", "recipe_id")
        VALUES
            (1, "2026-08-13 08:00:00", "breakfast", 1);
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

