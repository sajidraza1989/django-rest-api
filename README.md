Django Rest Framework(DRF)

**Installation**:
To work on DRF we need python and Django as prerequisite.
>pip instll python<Version>

>pip install django

then to work on Djonago Rest Framework install djandorestframework
>pip install djangorestframework

if you are using mysql DB then please install mysqlclient
>pip install mysqlclient

**Creating Project**: 

**Note**: django rest framework works with concept - one project with multiple app support

Fist we will create project and then app
>django-admin start-project myFirstRestProject

Go to that project cd myFirstRestProject and then create the app using below commond
>python manaage.py startapp myFirstRestApp

**Register the app with project and ret_framework**

open the settting.py of project, navigate to INSTALLED_APPS and Add the our app and rest_framework

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    **'rest_framework',
    'myFirstRestApp',**
]

**Create the views in our app :**

add the views in project under the url.py - urlPattern [] using path attribute

from myFirstRestApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    **path('test/', views.myFisrtRestRequest, name='myFirstRest'),**
]

**Run the server and hit the your view**
localhost:8080/test/

**Now see the Response:**

**Connecing to DB**
In Django, the default table name for a model is constructed as <app_label>_<model_name>, where <app_label> is the name of the app (in this case, myfirstrestapp), and <model_name> is the lowercase name of the model (employee). Therefore, the Employee model in the myFirstRestApp app is mapped to the myfirstrestapp_employee table in the database. This naming convention helps Django avoid table name conflicts across different apps.
_To avoid Django’s default behavior of naming tables as <app_name>_<model_name>, you can explicitly set the database table name for each model using the db_table option in the model’s **Meta class**._

# models.py
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    age = models.IntegerField()

    class Meta:
        db_table = 'employee'  # This will use 'employee' as the table name

#With this, Django will use employee as the table name instead of myfirstrestapp_employee.


