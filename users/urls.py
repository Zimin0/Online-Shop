from django.urls import path
from .views import home, SignUp, users_list

app_name = 'users'

urlpatterns = [
    path('', home, name="home"),
    path("signup/", SignUp.as_view(), name="signup"),
    path('users/', users_list, name='users'),
]

""" 
Urls, предоставляемые приложением auth

accounts/login/ [name='login']
accounts/logout/ [name='logout']
accounts/password_change/ [name='password_change']
accounts/password_change/done/ [name='password_change_done']
accounts/password_reset/ [name='password_reset']
accounts/password_reset/done/ [name='password_reset_done']
accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
accounts/reset/done/ [name='password_reset_complete']
"""