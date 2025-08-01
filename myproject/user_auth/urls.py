from django.urls import path
from user_auth import views

urlpatterns = [
    path('',views.login_,name='login'),
    path('registration',views.registration_page,name='registration'),
]
