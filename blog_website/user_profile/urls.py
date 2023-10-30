from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_user , name='login'),
    path('logout/', logout_user , name='logout'),
    path('register_user/', register_user , name='register_user'),
    path('profile/', profile , name='profile'),
    path('change_profile_picture/',change_profile_picture,name='change_profile_picture')

]