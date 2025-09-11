API endpoints:

/restaurant/menu           : Menu API(GET, POST, PUT, DELETE)
/restaurant/booking/tables : Booking API (ViewSet, Authenticated)
/auth/users/               : User registration (Djoser) - create user
/auth/token/login/         : Login to obtain token
/auth/token/logout/        : Lougout and revoke token 

Unit Testing:

After activating the environment run: python manage.py test tests

