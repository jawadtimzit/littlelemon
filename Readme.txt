To Run the aaplication on VS code in your local:
------------------------------------------------
1 - Clone repository and open in VS code (example clone to C:\Users\username\Documents\GitHub)
2 - Open terminal and cd to repo folder, once in directory where you cloned the application : example C:\Users\username\Documents\GitHub\littlelemon>
3 - Activate environement: While on repo folder littlelemon on VS terminal, run:
    -C:\Users\username\Documents\GitHub\littlelemon>py -m venv venv (This will create and venv folder), once this created run below  command
    -C:\Users\username\Documents\GitHub\littlelemon>venv\Scripts\activate 
4 - While env is activated and you see (venv) before directory repo folder on VS, Install dependencies: pip install -r requirements.txt 
5 - Update SQL Server credentials to match your local (use your SQL server databse name, username, and password) - These are credentials on Datbases block on setting.py.
6 - Run migrations:
   python manage.py makemigrations
   python manage.py migrate
7 - While activated and installation of requirements.txt is finished, Run application (venv)   C:\Users\username\Documents\GitHub\littlelemon>python manage.py runserver  
8 - Test below endpoints, root path http://127.0.0.1:8000/

API endpoints:
----------------------------------------------
/restaurant/menu           : Menu API(GET, POST, PUT, DELETE)
/restaurant/booking/tables : Booking API (ViewSet, Authenticated)
/auth/users/               : User registration (Djoser) - create user
/auth/token/login/         : Login to obtain token
/auth/token/logout/        : Lougout and revoke token 

Unit Testing:
----------------------------------------------
After activating the environment run: python manage.py test tests

Screnshots under folder:
---------------------------------------------
images/
 
