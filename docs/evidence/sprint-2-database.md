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

### Test 1 – Database starts correctly

### What I am testing:
Whether the database starts correctly when the application is launched.

###How I tested it:
I ran:
docker compose up
THen I checked the terminal output to make sure there were no database 
initialization errors.

Expected outcome:
The database should initialize successfully without errors.

Actual outcome:
Database schema
![Database schema](screenshots/database_schema_logs.png)

Database seeded data
![Database schema](screenshots/database_contents_logs.png)


### Test 2 – Database tables are created

### What I am testing:
Whether all required database tables are created.

### How I tested it:
I inspected the database after starting the application and checked for the following tables:

- users
- households
- household_members
- recipes
- meal_plan

### Expected outcome:
All five tables should exist.

### Actual outcome:
[Add your result here.]



## Testing User Registration and login 

Replace this text with notes about what you are testing, how you tested it, and the outcome of the testing
Testing the ability for a user to make an account and log in. I opened the user sign up form and then entered 
an email, username and password and then clicked the add user button. 
After this I logged in and then checked whether the nav bar shows that I am logged in

Test data: 
- Email - user@test.com
- Password - 1234
- username - user

#### Entering test data
![Signing up](screenshots/sign_up_test.png)

#### Confirmation of sign up
![Sign up confirmation](screenshots/sign_up_confirmation.png)

#### Entering test data to login 
![Logging in](screenshots/login_test.png)

#### Confirmation of login with flash message and nav showing username
![Login confirmation](screenshots/login_confirmation.png)



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


#### Entering test data
![Testing household creation](screenshots/household_creation_test.png)

#### Confirmation of household creation
![Flash message confirming household creation](screenshots/household_creation_confirmation.png)
![Navbar changes confirming household creation](screenshots/household_creation_confirmation_2.png)



### Changes / Improvements

#### Removed quotation marks around household name in confirmation flash
![Fixed household confirmation without quotation marks](screenshots/household_confirmation_fix.png)



## Sprint Review

Replace this text with a statement about how the sprint has moved the project forward - key success point, any things that didn't go so well, etc.

