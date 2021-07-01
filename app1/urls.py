from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . views import *
urlpatterns = [
    path('fake/',fake_generate_data,name="fake" ),
    path('excel_file_creation/',excel_file_creation,name="excel_file_creation" ),
    path('send_mail/',send_mail_with_attachment,name="send_mail" ),

]
