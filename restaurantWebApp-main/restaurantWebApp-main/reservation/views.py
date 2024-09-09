from django.shortcuts import render, redirect
from .models import Reservation, TokenModle
from .forms import ReserveTableForm, TokenForm
from django.contrib import messages
from django.forms.models import model_to_dict


def reserve_table(request):

    reserve_form = ReserveTableForm()

    if request.method == 'POST' :        
        reserve_form = ReserveTableForm(request.POST)
        
        #print(reserve_form.data.values)
        
        #print(reserve_form.fields.values)
        #your_name = reserve_form['name'].value() #reserve_form.fields(label="name", max_length=100)
        #print(your_name, "\n************\n")
      
        try:

            your_date = reserve_form['date'].value()

            

            from datetime import datetime
            format = "%Y-%m-%d"
            res = None
            try:
                res = bool(datetime.strptime(your_date, format))

                # Now let's compare the dates 
                passed_datetime = datetime.strptime(your_date, "%Y-%m-%d")
                now_time = datetime.now()

                if(passed_datetime < now_time):
                    messages.error(request, "Please enter correct date.")

            except ValueError as exc:
                res = False
            

            if res is False:
                messages.error(request, "Your entered date format not matched , please follow YYYY-MM-DD")


            your_time = reserve_form["time"].value()

            timeformat = "%H:%M"

            is_time_validate = None

            try:
                
                is_time_validate = datetime.strptime(your_time, timeformat)
            except:
                is_time_validate = False

            if is_time_validate is False:
                messages.error(request, "Your entered time format not matched , please follow H:MM")

            return render(request , 'reservation.html' , context)  
        
        except Exception as exc:
            print(exc,"\n*******\n")


            if reserve_form.is_valid():
                Reservation.objects.create(user=request.user, number_of_persons=reserve_form['number_of_persons'].value(), date=reserve_form['date'].value(), time=reserve_form['time'].value())
                messages.success(request, "Your Reservation is Successfully Completed.")

            context = {'form' : reserve_form}
            
            return render(request , 'reservation.html' , context)
    else:
        context = {'form' : reserve_form}
        return render(request , 'reservation.html' , context)  



def customer_detail(request):
    if request.user.is_authenticated:
        detail = Reservation.objects.filter(user__id = request.user.id)
    else:
        messages.error(request, "You must be logged in to see reservations made by you!")
        detail = None

    context = {'detail':detail}
    return render(request , 'user_detail.html' , context)
 
 
def delete_reservation(request , id):
    
    delete1 =  Reservation.objects.get(pk=id)
    delete1.delete()
    messages.success(request, "Your Reservation is Cancel.")
    return redirect('reservation:user_detail')

def edit_reservation(request, id):
    if request.method == 'POST':
        reservation_form = ReserveTableForm(request.POST)
        
        if reservation_form.is_valid():
            reservation = Reservation.objects.get(id=id)
            reservation.number_of_persons = reservation_form['number_of_persons'].value()
            reservation.date = reservation_form['date'].value()
            reservation.time = reservation_form['time'].value()
            reservation.save()

            messages.success(request, 'Updated reservation successfully!')
            return redirect('reservation:user_detail')
        else:
            messages.error(request, 'Something happened, make sure to follow provided format.')

    reservation = Reservation.objects.get(id=id)
    reservation_form = ReserveTableForm(initial=model_to_dict(reservation))

    context = {
        'form': reservation_form
    }

    return render(request, 'edit_reservation.html', context)
