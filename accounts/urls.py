from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns=[
    path('login', views.login, name='login_user'),
    path('logout', views.logout, name='logout_user'),
    path('signup', views.signup, name='signup_user'),
    path('me', views.me, name='me'),
    path('me/edit', views.edit_account, name='edit_account'),
    path('me/change_password', views.change_password, name='change_password')
]
