from django.shortcuts import render
from .models import AboutUs, WhyChooseUs, Chef


def aboutus_list(request):
    """
        @rajaSaheebFayyaz.
        Loading dependency required to load the about us section successfuly.
    """
    about = AboutUs.objects.last()
    why_choose_us = WhyChooseUs.objects.all()
    chef = Chef.objects.all()

    context = {
        'about' : about ,
        'why_choose_us' : why_choose_us ,
        'chef' : chef,
    }

    # @rajaSaheebFayyaz. : rendering aboutus template defined in current folder template .html files
    return render(request , 'about.html' , context)
