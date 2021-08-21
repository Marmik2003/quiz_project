# quiz_project
Steps to run this project
1. Make virtual environment using 
    `virtualenv venv`
2. Enter virtual environment
3. Install requirements using `pip install -r requirements.txt`
4. Run `python manage.py makemigrations`
5. Run `python manage.py migrate`
6. Run `python manage.py createsuperuser` for login
7. Run `python manage.py runserver`
8. Now you can open localhost http://127.0.0.1:8000/login/
