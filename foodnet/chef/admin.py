from django.contrib import admin
from .models import Chef,ChefExpertiseArea,ChefDoc,Event,EventRegistration,ChefRecipe,ChefRecipeImage,ChefRecipeLike,ChefRecipeFeedback,ChefFollower,UserRecipesValidation
# Register your models here.
admin.site.register(Chef)
admin.site.register(ChefExpertiseArea)
admin.site.register(ChefDoc)
admin.site.register(Event)
admin.site.register(EventRegistration)
admin.site.register(ChefRecipe)
admin.site.register(ChefRecipeImage)
admin.site.register(ChefRecipeLike)
admin.site.register(ChefRecipeFeedback)
admin.site.register(ChefFollower)
admin.site.register(UserRecipesValidation)