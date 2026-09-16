# Sprint 3 - Developing a Minimum Viable Product (MVP)


## Sprint Goals

Continue to develop the web application to the point that it provides all key 
functionality of the system. Test and refine it so that it can serve as the basis 
for the final phase of development.

### Specific Goals

- Create the following web pages:
    - Household management
    - Full meal plan

- Develop SQL database queries to:
    - Add a new meal to a day in meal plan
    - Delete a user from a household
    - Delete a household
    - Transfer household ownership


## Testing Household management    

I will test the household management functionality to ensure that users can 
interact with households after the basic household creation functionality 
implemented in Sprint 2

Testing will include:

- Joining an existing household using a join code
- Entering an invalid join code
- Displaying household members
- Removing household members where permitted
- Transferring household ownership where permitted
- Leaving a household
- Deleting a household

Expected outcome:

Users should be able to join and manage their household according to their permissions. 
Invalid actions should be prevented and the application should provide clear feedback 
when an action cannot be completed

Actual outcome



### Changes / Improvements

Replace this text with notes any improvements you made as a result of the testing



## Testing Meal Plan Management

I am testing the meal plan functionality to make sure meals can be added and removed 
correctly and that two meals cannot be added to the same meal type on the same date

How I tested it:

I logged in as a test user and opened the meal plan page

I then:

- Added a recipe to the meal plan
- Checked that the meal appeared on the correct date
- Tried to add another meal to the same date and meal type
- Added a meal to a different meal type
- Removed a meal from the meal plan

Expected result:

meal should appear on the selected date and meal type

The application should prevent two meals from being added to the same date and meal type

Meals with different meal types should be allowed on the same date

A meal should be removed when the delete option is used
Actual outcome:
Adding a meal

Duplicate meal prevented

Meal plan displaying meals

Removing a meal

Changes/Improvements
- Added a delete option for meals.


## Testing Household Permissions

I am testing whether household permissions work correctly for owners and normal members

How I tested it:
I created a household with one user as the owner and joined the household using a second test account

I tested the following actions as the normal member via the UI and entering the route manually:

- Removing another member
- Transferring ownership
- Deleting the household

I then tested the same actions while logged in as the owner.
Expected result:

The owner should be able to manage the household

A normal member should not be able to perform owner only actions

The application should display an error message when a user attempts an action they do not have permission to perform

Actual outcome:
Normal member attempting owner action

Owner managing household


## Testing Household Deletion

I am testing whether the household owner can delete a household and whether the related household data is removed correctly.
How I tested it:

I logged in as the household owner and opened the household management page

I clicked the delete household option

I then checked that:

- The household was deleted
- Household members were removed
- The household recipes were removed
- The household meal plan was removed
- The user was no longer shown as being in a household

Expected result:

The household should be deleted only when the owner requests the deletion

The user should no longer belong to the deleted household

The household's recipes and meal plan entries should also be removed

Actual outcome:

Changes / Improvements

    Added a permission check so only the household owner can delete the household.

    Added deletion of household recipes and meal plans.

    Removed household memberships when the household is deleted.

    Updated the user's session after deletion.

    Added a confirmation flash message.


## Testing FEATURE NAME HERE

Replace this text with notes about what you are testing, how you tested it, and the outcome of the testing

**PLACE SCREENSHOTS AND/OR ANIMATED GIFS OF THE TESTING HERE**

### Changes / Improvements

Replace this text with notes any improvements you made as a result of the testing.

**PLACE SCREENSHOTS AND/OR ANIMATED GIFS OF THE IMPROVED SYSTEM HERE**


## Testing FEATURE NAME HERE

Replace this text with notes about what you are testing, how you tested it, and the outcome of the testing

**PLACE SCREENSHOTS AND/OR ANIMATED GIFS OF THE TESTING HERE**

### Changes / Improvements

Replace this text with notes any improvements you made as a result of the testing.

**PLACE SCREENSHOTS AND/OR ANIMATED GIFS OF THE IMPROVED SYSTEM HERE**


## ETC...


## Sprint Review

Replace this text with a statement about how the sprint has moved the project forward - key success point, any things that didn't go so well, etc.

