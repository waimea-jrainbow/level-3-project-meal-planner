# Sprint 4 - Developing a Refined and Complete System


## Sprint Goals

Develop the system until it is fully featured, with a refined UI and it satisfies the requirements. 
The system will be fully tested at this point.

### Specific Goals

- Refine the design and UI of the website
- Refine the user experience (UX) of the system
- Perform final, full-system testing
- Get user feedback throughout on all of the above


## User feedback

#### floating forms vs separate page forms

"Floating is better"


## Testing Floating HTMX sign up and login forms

Testing the sign up and login forms appearing overlaid over the rest of the page and closing when clicked outside of

![Clicking Login button and then clicking outside of it then repeating for sign up](screenshots/floating_forms_outside_click_test.webp)

Testing the sign up and login forms closing after clicking the cancel button

![Clicking Login button and then clicking cancel button then attempting to repeat for sign up](screenshots/floating_forms_cancel_test.webp)
Can't open another form after cancelling one

### Changes / Improvements

Changed the HTMX to innerHTML so it only replaces the contents of the div instead of the div itself
![Clicking Login button and then clicking cancel button then repeating for sign up](screenshots/floating)


## Testing Dashboard

Added a dashboard for when the user is logged in. Needs to show fields for joining and creating a household
when user isn't in a household and show household details when they are in a household

![Screenshot of dashboard](screenshots/dashboard_refined.png)


## User feedback

Asked end-user what design ideas they had for manage recipes page as it was quite bland in refined ui prototype

Came up with this option here compared to original 

![Image showing 2 manage recipe page designs](screenshots/manage_recipe_options.png)


## User feedback

Showed end user progress on manage members section of manage household. Received feedback that it didn't seem quite right
after some ideation came up with a crown or person icon on the left side of the name to designate owner or member


![Screenshot of first iteration of member info section](screenshots/1st_member_info.png)

![Screenshot of second iteration of member info section](screenshots/2nd_member_info.png)



## Sprint Review

This sprint was went very well as I've produced an aesthetic and layout that I am very happy
with but because of my very verbose testing in previous sprints I've struggled to find things to test in this sprint

