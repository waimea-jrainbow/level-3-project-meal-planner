# Sprint 2 - Implement Database and Display of Test Data


## Sprint Goals

Implement the database, populated with test data. Create queries that retrieve test data, and display this on web pages as needed. Test and refine the queries and data display, so that it stands as the basis of the next sprint.

### Specific Goals

- Implement the database
- Add test data to the database
- Create the following web pages:
    - Home pages showing...
    - Details page for ...
    - Etc.
- Develop SQL database queries to:
    - Retrieve all ...
    - Retrieve specific ...
    - Etc.


## Testing Database initialization
I tested whether the SQLite database initializes correctly when the application is started using 
docker compose. I checked that all required tables were created and that the database was populated
with the expected seed data.

### How I tested it:
I ran:
docker compose up
Then I checked the terminal output to make sure there were no database 
initialization errors and that seed data was present.

Expected outcome:
The database should initialize successfully without errors and be populated with seed data.

Actual outcome:

Database schema

![Database schema](screenshots/database_schema_logs.png)

Database seeded data

![Database schema](screenshots/database_contents_logs.png)


## Testing User Registration and login 
Testing the ability for a user to make an account and log in. 

### How I tested it:
I opened the sign-up page and entered:

    Email: user@test.com
    Username: user
    Password: 1234

I then clicked Add user.

### Expected result:
The account should be created and the user should be redirected to the login page with a confirmation message.

Actual outcome:
#### Entering test data
![Signing up](screenshots/sign_up_test.png)

#### Confirmation of sign up
![Sign up confirmation](screenshots/sign_up_confirmation.png)

#### Entering test data to login 
![Logging in](screenshots/login_test.png)

#### Confirmation of login with flash message and nav showing username
![Login confirmation](screenshots/login_confirmation.png)


## Testing duplicate email registration
Testing whether the application prevents a second account from being 
created using an email address that already exists.

How I tested it:
I attempted to create another account using:

    Email: user@test.com
    Username: anotheruser
    Password: 1234

![Entering duplicate email user](screenshots/duplicate_email_data.png)

Expected result:
The account should not be created. The application should display an error 
message stating that an account using the email address already exists.

Actual outcome:

#### Duplicate is refused but user is not routed back to form and flash message has quotation marks around email
![Duplicate email outcome](screenshots/duplicate_email_outcome.png)

### Changes / Improvements

#### Correct routing from submitting bad data and removed quotation marks
![Corrected routing and removed quotation marks](screenshots/dupliacte_email_fix.png)



## Testing Household Creation

I am testing household creation, more specifically:
- logged-in user can open the join/create household page
- household name is required
- unique six-digit join code is generated
- household is inserted into the database
- creator is automatically added as an owner
- session is updated with the household information

to do this I logged in as a test user then clicked the house holds button in the navbar from 
here I entered testhouse as the household name and clicked submit from there I checked the 
navbar as well and the confirmation flash message to confirm test user is in a household 


#### Entering test data
![Testing household creation](screenshots/household_creation_test.png)

#### Confirmation of household creation
![Flash message confirming household creation](screenshots/household_creation_confirmation.png)
![Navbar changes confirming household creation](screenshots/household_creation_confirmation_2.png)



### Changes / Improvements

#### Removed quotation marks around household name in confirmation flash
![Fixed household confirmation without quotation marks](screenshots/household_confirmation_fix.png)


## Testing recipe creation and image upload

I am testing the creation of a recipe:
- The page opens
- data can be entered
- recipe is saved to database
- image can be uploaded
- 

to do this I logged in as a test user went to the add recipe page then entered the test data

- name: test recipe
- link:testrecipe.com
- image: hamburger.png 
![Hamburger icon](screenshots/hamburger.png)
- meal type: dinner


#### Entering test data
![Entering test data for recipe](screenshots/add_recipe.png)

#### Confirmation of recipe creation
![Flash message confirming recipe creation](screenshots/add_recipe_confirmation.png)
![Recipe shows in recipe list confirming recipe creation](screenshots/add_recipe_confirmation_2.png)


### Changes / Improvements

#### Removed quotation marks around household name in flash and reworded confirmation flash message
![Fixed household confirmation without quotation marks](screenshots/add_recipe_fix.png)

#### Changed name of link input in html form from Link to link


## Testing recipe creation and image upload

I am testing the creation of a recipe:
- The page opens
- data can be entered
- recipe is saved to database
- image can be uploaded


to do this I logged in as a test user went to the add recipe page then entered the test data

- name: test recipe
- link:testrecipe.com
- image: hamburger.png 
![Hamburger icon](screenshots/hamburger.png)
- meal type: dinner


#### Entering test data for link recipe
![Entering test data for link recipe](screenshots/add_recipe.png)

#### Entering test data for manual recipe
![Entering test data for manual recipe](screenshots/add_recipe_manual_test.png)

#### Confirmation of recipe creation
![Flash message confirming recipe creation](screenshots/add_recipe_confirmation.png)
![Recipe shows in recipe list confirming recipe creation](screenshots/add_recipe_confirmation_2.png)


### Changes / Improvements

#### Removed quotation marks around household name in flash and reworded confirmation flash message
![Fixed household confirmation without quotation marks](screenshots/add_recipe_fix.png)

#### Changed name of link input in html form from Link to link

#### Added text area closing tags on manual recipe so method code isn't inside ingredients
![Fixed manual recipe add form](screenshots/add_recipe_manual_fix.png)

## Testing image creation with non ideal test data

Testing what happens when test data is not expected data
- No title
- No url
- No image

#### Form is not submitted if title or url are missing
![No title and no url tests for recipe](screenshots/unexpected_data_recipe.png)

#### Form is submitted but error is shown
![No image test for recipe](screenshots/no_image_recipe.png)

### Changes / Improvements

- Changed form so it will not submit when there is no image 
![Error message when no image is provided](screenshots/add_recipe_fix_2.png)



## Recipe retrieval and display

Testing whether list of recipes is displayed correctly and if individual recipe's
details are displayed correctly  

I viewed the recipe list and an individual recipe after adding multiple test recipes

#### List of recipes: images do not show
![List of recipes](screenshots/recipes_display_test.png)

#### Individual link recipe: images do not show, links try to go to route not external page
![Individual link recipe](screenshots/recipe_display_test.png)

#### Individual manual recipe
![Individual manual recipe](screenshots/recipe_display_manual_test.png)


### Changes / Improvements

#### removed app from the front of image_path so recipe images show
![Recipe list fixed](screenshots/recipes_display_fix.png)

#### Added code in recipe route to add https:// to the start of links without it and added target="_blank" so link opens in new tab

#### Added code to individual recipe to not display links if not existent and vice versa

#### Added code in individual recipe to list ingredients and method of manual recipe in an actual list
![Method and ingredients listed in actual lists](screenshots/recipe_display_manual_fix.png)


## Adding meals to meal plan

Testing whether I can add a meal to a date and that the multiple meals can be set for the same date and time



## Meal plan retrieval and display

Testing whether meal plan pulls meals on dates correctly and displays them

I viewed the meal plan 

## Sprint Review

Replace this text with a statement about how the sprint has moved the project forward - key success point, any things that didn't go so well, etc.

