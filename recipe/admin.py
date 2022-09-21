from django.contrib import admin
from .models import recipe
# Register your models here.
# admin.site.register(recipe)

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('recipe_pic','recipe_name')
    search_fields = ('recipe_name',)
    list_per_page =20


admin.site.register(recipe,RecipeAdmin)