
from django.contrib import admin
from django.urls import path
from app01 import views
urlpatterns = [
    #path('login',admin),
    path('tutor/',views.tutor),
    path('add_tutor/',views.add_tutor),
    path('edit_tutor/',views.edit_tutor),
    path('del_tutor/',views.del_tutor),
]
