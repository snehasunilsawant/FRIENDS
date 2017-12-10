# FRIENDS
Django Based social networking website

**Scope**: 
Implemented multi-page website from scratch (using RESTful routing/Web APIs, MVC, user authentication (login/registration), front and backend validations, backend DB with basic CRUD) Focus was to integrate multiple APIs into project and move the item through front end to back end.

## Environment:
```
Framework : django
Database : MySQL and ORM
Languages : python
CSS Framework : materialiseCSS
```
## Features :
1. User should able to register and login to website sucessfully. For incorrect inpute proper user friendly messages/pop-up should get displayed

2. Website Dashboard should consist of :
      * List of all friends ( logged in user's connections)
      * User can view friend's profile or can remove as friend.
      * List of all other users ( Not Friends)
      * User can view other user's profile and can add them as friend.

3. User Profile : User profile displays all user details.

4. If User A becomes friends with User B , User B will automatically will become friends with User A

5. Logged in user should able to navigate Home/Dashboard page or logout anytime.

## Implemetation : 
1. A fully functional login and registration app! This combines MVC patterns, validations, and password encryption.
   - Show validation error messages if validations fail the following tests
   - First Name - Required; No fewer than 2 characters; letters only
   - Last Name - Required; No fewer than 2 characters; letters only
   - Email - Required; Valid Format
   - Password - Required; No fewer than 8 characters in length; matches Password Confirmation
   - Birthday - Before today, or go creative and do it in an age range
