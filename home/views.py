from django.shortcuts import render
# from meals.models import Meal , Category
# from blog.models import Post
# from aboutus.models import WhyChooseUs


def home(request):

    
    """
        @rajaHaseebFayyaz
        Passing created index.html to be render on home page loading.
    """
    

    context = None

    return render(request , 'index.html' , context)
