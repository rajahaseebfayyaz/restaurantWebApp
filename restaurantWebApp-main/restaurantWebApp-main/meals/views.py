from django.shortcuts import render

from .models import Meal, Category

# Create your views here.

def meal_list(request):
    """
     List meals and their categories. This is a view for the admin to view and edit meals
     
     @param request - Django request object ( Required )
     
     @return The template context to render the meals / list. html
    """
    meal_list = Meal.objects.all()
    categories = Category.objects.all()
    context = {
        'meal_list': meal_list,
        'categories': categories,
        }
    return render(request, 'meals/list.html', context)

def meal_detail(request, slug):
    """
     Renders meal detail page. It is used to display details of a meal
     
     @param request - Django request object ( Required )
     @param slug - Slug of the meeting you want to display.
     
     @return Rendered Meal detail page ( Optional ) or error
    """
    meal_detail = Meal.objects.get(slug=slug)

    context = {'meal_detail' : meal_detail}
    return render(request, 'meals/detail.html', context=context)
