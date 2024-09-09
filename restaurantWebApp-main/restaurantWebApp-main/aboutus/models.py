from django.db import models

# Create your models here.

class AboutUs(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    #image = models.ImageField(upload_to='aboutus/', null=True)

    class Meta:
        verbose_name = 'about us'
        verbose_name_plural = 'about us'

    def __str__(self) -> str:

        """
         Returns the title of the file. This is useful for debugging and to avoid having to re - write the file in a way that can be reproducible.
         
         
         @return The title of the file as a string or None if it cannot be
        """

        return self.title


class WhyChooseUs(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    class Meta:
        verbose_name = 'why choose us'
        verbose_name_plural = 'why choose us'

    def __str__(self) -> str:
        """
            Returns the title of the file. This is useful for debugging and to avoid having to re - write the file in a way that can be reproducible.
            
            
            @return The title of the file as a string or None if it cannot be
        """
        return self.title


class Chef(models.Model):
    name = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='chef/')

    class Meta:
        verbose_name = 'chef'
        verbose_name_plural = 'chefs'

    def __str__(self) -> str:
        """
         Returns the name of the feature. This is used to generate human readability and visual inspection of the feature's name.
         
         
         @return The name of the feature as a string e. g
        """
        return self.name
