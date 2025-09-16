To Run the aaplication on VS code in your local:

-Clone repository and open in VS code (example clone to C:\Users\username\Documents\GitHub)
-Open terminal and cd to repo folder, once in directory where you cloned the application : example C:\Users\username\Documents\GitHub\littlelemon>
-Activate environement by runing C:\Users\username\Documents\GitHub\littlelemon>venv\Scripts\activate 
-Once env activated, Run application (venv) C:\Users\username\Documents\GitHub\littlelemon>python manage.py runserver  
-Update SQL Server credentials to match your local (use your SQL server username and password)
-Test below endpoints, root path http://127.0.0.1:8000/

API endpoints:

/restaurant/menu           : Menu API(GET, POST, PUT, DELETE)
/restaurant/booking/tables : Booking API (ViewSet, Authenticated)
/auth/users/               : User registration (Djoser) - create user
/auth/token/login/         : Login to obtain token
/auth/token/logout/        : Lougout and revoke token 

Unit Testing:

After activating the environment run: python manage.py test tests

Screnshots under folder:
images/
 