from django.contrib import admin
from .models import EndUser,EndUserRecipe,EndUserRecipeImage,EndUserRecipeLike,EndUserRecipeFeedback,EndUserFollower
# Register your models here.
admin.site.register(EndUser)
admin.site.register(EndUserRecipe)
admin.site.register(EndUserRecipeImage)
admin.site.register(EndUserRecipeLike)
admin.site.register(EndUserRecipeFeedback)
admin.site.register(EndUserFollower)