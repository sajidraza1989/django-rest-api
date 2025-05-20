Django Rest Framework(DRF)

**Installation: **
To work on DRF we need python and Django as prerequisite.
>pip instll python<Version>

>pip install django

then to work on Djonago Rest Framework install djandorestframework
>pip install djangorestframework

if you are using mysql DB then please install mysqlclient
>pip install mysqlclient

**Creating Project -** 

Note: in django rest framework - work with concept - one project with multimple app support

Fist we will create project and then app
>django-admin start-project myFirstRestProject

Go to that project cd myFirstRestProject and then create the app using below commond
>python manaage.py startapp myFirstRestApp

**Register the app with project and ret_framework**
open the settting.py of project
navigate to INSTALLED_APPS
and Add the our app and rest_framework

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

**add the views in project under the url.py - urlPattern [] using path attribute**

from myFirstRestApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    **path('test/', views.myFisrtRestRequest, name='myFirstRest'),**
]

**Run the server and hit the your view**
localhost:8080/test/

**now see the Response:**



