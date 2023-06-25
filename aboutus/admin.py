
# Register all nodes that have an AboutUs WhyChooseUs and Chef

from django.contrib import admin

from .models import AboutUs, WhyChooseUs, Chef


admin.site.register(AboutUs)
admin.site.register(WhyChooseUs)
admin.site.register(Chef)
