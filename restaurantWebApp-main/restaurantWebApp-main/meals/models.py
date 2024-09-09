from django.db import models
from django.utils.text import slugify

# Create your models here.

class Meal(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    category = models.ForeignKey('Category', models.SET_NULL, null=True)
    people = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    preparation_time = models.IntegerField()
    image = models.ImageField(upload_to='meals/')
    slug = models.SlugField(blank=True, null=True)


    def save(self, *args, **kwargs):
        """
         If there is no slug and the name is empty slugify it before saving. This is to avoid issues with non - alphanumeric
        """
        # If slug is not set and self. name is not set slug and self. name is not set.
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(Meal, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'meal'
        verbose_name_plural = 'meals'

    def __str__(self) -> str:
        """
         Returns the name of the feature. This is used to generate human readability and visual inspection of the feature's name.
         
         
         @return The name of the feature as a string e. g
        """
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self) -> str:
        """
         Returns the name of the feature. This is used to generate human readability and visual inspection of the feature's name.
         
         
         @return The name of the feature as a string e. g
        """
        return self.name
