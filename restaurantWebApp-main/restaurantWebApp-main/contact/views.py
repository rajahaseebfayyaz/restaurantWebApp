from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

from .forms import ContactForm
from django.urls import reverse
from django.contrib import messages

def send_email(request):
    if request.method == 'PsOST':
        form = ContactForm(request.POST)
        print("triggered here", '\n')
    else:
        print("triggered in else", '\n')
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            reciepient_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']

            try :
                recipient_list = [reciepient_email]
                from_email = "sharmaomesh0@gmail.com"
                send_mail(name, message,from_email, recipient_list)
                messages.success(request, "Your Reservation is Successfully Completed.")

            #except BadHeaderError:
            except :
                #return reverse('contact:send_success')
                messages.success(request, "We are unable to complete your request now due to server issue , please try again later in few time.")
                #return HttpResponse('invalid header')

            #return HttpResponseRedirect('contact:send_success')
            #return reverse('contact:send_success')
            #return HttpResponseRedirect(reverse('news:home'))
        else:
            #messages.success(request, "Your form is not valid , please check the form fields.")
            pass

    context = {
        'form': form,
    }

    return render(request, 'contact.html', context)


def send_success(request):
     return HttpResponse('thanks you for your email ^_^')

def send_failure(request):
     return HttpResponse('thanks you for your email, currently our server is down , please try again later after some time. ^_^')
