from django.urls import path, include
from . import views


app_name= "Accounts"
urlpatterns = [
    path('register',views.register_user,name="register_user")
]
