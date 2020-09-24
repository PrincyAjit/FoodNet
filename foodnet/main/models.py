from django.db import models

# Create your models here.
class RecipeCategory(models.Model):
	category_name=models.CharField(max_length=50,unique=True)
	category_image=models.ImageField(default=None,upload_to='main_images/')
	category_slug=models.CharField(max_length=200,default=1,unique=True)
	# def __str__(self): #overriding string method that generally returns the object
	# 	return self.category_name

class GeneralRecipe(models.Model):
	recipe_name=models.CharField(max_length=30)
	recipe_description=models.CharField(max_length=200)
	category=models.ForeignKey(RecipeCategory,null=True,verbose_name="RecipeCategory",on_delete=models.SET_NULL) #either searches for same name field,or considers the primary key of the model
	ingredient_list=models.TextField()
	recipe_procedure=models.TextField()
	no_servings=models.PositiveIntegerField()
	prep_time=models.CharField(max_length=30) #mins/hrs
	cook_time=models.CharField(max_length=30) #mins/hrs
	image=models.ImageField(upload_to='main_images/')
	video=models.TextField(default=1) #copying youtube video directly,so no need filefield
	veg_nonveg=models.CharField(max_length=10) #veg,non-veg
	recipe_slug=models.CharField(max_length=200,default=1)

class ApplianceCategory(models.Model):
	category_name=models.CharField(max_length=50,unique=True)
	category_image=models.ImageField(default=None,upload_to='main_images/appliances')
	category_slug=models.CharField(max_length=200,default=1,unique=True)
	class Meta:
		verbose_name_plural="Appliance Catogories"
	def __str__(self): #overriding string method that generally returns the object
		return self.category_name

class Appliance(models.Model):
    appliance_category=models.ForeignKey(ApplianceCategory,null=True,verbose_name="ApplianceCategory",on_delete=models.SET_NULL) #if null true then it stores empty values as null
    appliance_name=models.CharField(max_length=30)
    appliance_description=models.CharField(max_length=200)
    appliance_image=models.ImageField(upload_to='main_images/appliances')
    purchase_link=models.URLField(max_length=500)
    # appliance_slug=models.CharField(max_length=200,default=1)

 