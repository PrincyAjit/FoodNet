from django.contrib import admin
from .models import GeneralRecipe,RecipeCategory,Appliance, ApplianceCategory
from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.

class GeneralRecipesAdmin(admin.ModelAdmin):
	fieldsets=[("general_info",{"fields":["recipe_name","recipe_description","category","no_servings","prep_time","cook_time","veg_nonveg"]}),
				("details",{"fields":["ingredient_list","recipe_procedure","image","recipe_slug"]})]
	formfield_overrides={models.TextField:{'widget':TinyMCE()}}	#get the tinymce editor for all TextFields

class ApplianceAdmin(admin.ModelAdmin):
    fieldsets=[("Info",{"fields":["appliance_category","appliance_name","appliance_description"]}),
				("Content",{"fields":["appliance_image","purchase_link"]})]

admin.site.register(GeneralRecipe,GeneralRecipesAdmin)
admin.site.register(RecipeCategory)
admin.site.register(Appliance, ApplianceAdmin)
admin.site.register(ApplianceCategory)