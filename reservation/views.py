from django.shortcuts import render
from .models import Reservation
from .forms import ReserveTableForm
from django.contrib import messages


def reserve_table(request):
    reserve_form = ReserveTableForm()

    if request.method == 'POST' :
        reserve_form = ReserveTableForm(request.POST)

        if reserve_form.is_valid():
            reserve_form.save()
        messages.success(request, "Your Reservation is Successfully Completed.")
    context = {'form' : reserve_form}

    return render(request , 'reservation.html' , context)




def customer_detail(request):
     detail = Reservation.objects.all()
     context = {'detail':detail}
     return render(request , 'user_detail.html' , context)
 
 
def delete_reservation(request , id):
    
    delete1 =  Reservation.objects.get(pk=id)
    delete1.delete()
    messages.success(request, "Your Reservation is Cancel.")
    return render(request , 'user_detail.html')


