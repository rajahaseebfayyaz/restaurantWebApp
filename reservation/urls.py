from django.urls import path
from . import views

app_name = 'reservation'

urlpatterns = [
    path('', views.reserve_table, name='reserve_table'),
     path('user_detail', views.customer_detail, name='user_detail'),
         path('delete_reservation/<int:id>', views.delete_reservation, name='delete_reservation'),
]
