# Django-Assesment

## Setup Instructions
 **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd vendor_management_system
   
##Change the db name and password in setting file
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_name',
        'USER': 'db_user',
        'PASSWORD': 'db_password',
        'HOST': 'db_host',
        'PORT': 5432,
    }
}
##Create Env
python3 -m venv env
source env/bin/activate 
##install requirment
pip install -r requirements.txt
##apply migration and createsuperuser
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

###API Endpoints###
navigate to url - http://127.0.0.1:8020/api/swagger/

there will available for all api endpoints
Now u can able to create, view and update the vendor and po





