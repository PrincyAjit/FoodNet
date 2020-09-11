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
	veg_nonveg=models.CharField(max_length=10) #veg,non-veg
	recipe_slug=models.CharField(max_length=200,default=1)

class Appliance(models.Model):
	appliance_name=models.CharField(max_length=30)
	appliance_image=models.ImageField(upload_to='main_images/')
	appliance_description=models.CharField(max_length=200)
	purchase_link=models.URLField(max_length=200)

 