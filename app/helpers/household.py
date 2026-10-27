#===========================================================
# Auth Related Functions
#===========================================================

from flask import redirect, session, flash
from functools import wraps


#-----------------------------------------------------------
# A decorator function to check if user in household
# - This is determined by a 'in_household' value being present
#   in the session
#-----------------------------------------------------------
def household_required(func):
    @wraps(func)
    # Wrap a given function...
    def wrapper(*args, **kwargs):

        # Is the user logged in?
        if session.get('in_household'):
            # Yes, so run function
            return func(*args, **kwargs)

        # No, so go to home page
        flash("You need to be part of a household", "error")
        return redirect("/household")

    return wrapper


