from django.contrib import admin
from .models import GeneralRecipe,RecipeCategory,Appliance
from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.

class GeneralRecipesAdmin(admin.ModelAdmin):
	fieldsets=[("general_info",{"fields":["recipe_name","recipe_description","category","no_servings","prep_time","cook_time","veg_nonveg"]}),
				("details",{"fields":["ingredient_list","recipe_procedure","image","recipe_slug"]})]
	formfield_overrides={models.TextField:{'widget':TinyMCE()}}	#get the tinymce editor for all TextFields
admin.site.register(GeneralRecipe,GeneralRecipesAdmin)
admin.site.register(RecipeCategory)
admin.site.register(Appliance)