# django-blog
Magazine Blog with Django Framework
py -m pip install pymysql
add to __init__ same dir setting.py
import pymysql

pymysql.install_as_MySQLdb()


py -m pip install django-ckeditor --upgrade
py -m pip install django-debug-toolbar
py -m pip install django-admin-interface

mysql database name: mymagazine

py manage.py migrate 
py manage.py createsuperuser
py manage.py runserver