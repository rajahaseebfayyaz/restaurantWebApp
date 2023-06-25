from django.shortcuts import render
from meals.models import Meal


def home(request):

    meals = Meal.objects.all()
    
    """
        @rajaHaseebFayyaz
        Passing created index.html to be render on home page loading.
    """
    

    context = {
        'meals' : meals
    }

    return render(request , 'index.html' , context)
