from django.urls import path
from . import views



app_name = 'home'

"""
    @rajaHaseebFayyaz
    urlpatterns will decide which sub page to be handled from the home page.
"""
urlpatterns = [
    path('',views.home , name='home' ),
]
