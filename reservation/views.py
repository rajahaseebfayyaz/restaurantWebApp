from django.shortcuts import render
from .models import Reservation
from .forms import ReserveTableForm
from django.contrib import messages


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
            format = "%d/%m/%Y"
            res = None
            try:
                res = bool(datetime.strptime(your_date, format))

                # Now let's compare the dates 
                passed_datetime = datetime.strptime(your_date, "%d/%m/%Y")
                now_time = datetime.now()

                if(passed_datetime < now_time):
                    messages.error(request, "Please enter correct date.")

            except ValueError as exc:
                res = False
            

            if res is False:
                messages.error(request, "Your entered date format not matched , please follow dd/mm/yyyy")


            your_time = reserve_form["time"].value()

            timeformat = "%H:%M"

            is_time_validate = None

            try:
                
                is_time_validate = datetime.strptime(your_time, timeformat)
            except:
                is_time_validate = False

            if is_time_validate is False:
                messages.error(request, "Your entered time format not matched , please follow H:MM")


            your_phone = reserve_form['phone'].value()
            

            if(len(your_phone)) < 10 or len(your_phone) > 10:
                print(your_phone)
                messages.error(request, "Your phone number field entered is not correct, please check and try again.")
            else:
                if reserve_form.is_valid():
                    reserve_form.save()
                    messages.success(request, "Your Reservation is Successfully Completed.")

            context = {'form' : reserve_form}
            return render(request , 'reservation.html' , context)
        except Exception as exc:
            print(exc,"\n*******\n")


            if reserve_form.is_valid():
                reserve_form.save()
            messages.success(request, "Your Reservation is Successfully Completed.")
            context = {'form' : reserve_form}
            
            return render(request , 'reservation.html' , context)
    else:
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


