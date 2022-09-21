from django.db import models
from django.utils.html import format_html
from django.contrib.auth.models import User
# # Create your models here.
#
class recipe(models.Model):
    recipe_name = models.CharField(max_length=120)
    ingredient = models.CharField(max_length=1000)
    category = models.CharField(max_length=120)
    recipe_pic = models.ImageField(upload_to="images")
    How_to_make = models.CharField(max_length=1000)
    # url = models.CharField(max_length=100)
    # created_by = models.ForeignKey(to=User,on_delete=models.CASCADE)


    def __str__(self):
        return self.recipe_name

    def image_tag(self):
        return format_html('<img scr="/media/{}"/>'.format(self.image))



