from django.db import models
from main.models import RecipeCategory
import datetime,django
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# Create your models here.
class EndUser(models.Model):
    enduser_name=models.CharField(max_length=30)
    enduser_email=models.EmailField(unique=True)
    enduser_dob=models.DateField(default=datetime.date.today)
    enduser_password=models.CharField(max_length=15)
    enduser_photo=models.ImageField(upload_to='enduser_images/')
    enduser_country=models.CharField(max_length=50,default=None)
    enduser_state=models.CharField(max_length=50,default=None)
    enduser_city=models.CharField(max_length=50,default=None)
    enduser_bio=models.TextField()
    # def __str__(self): #overriding string method that generally returns the object
	#     return self.enduser_id
    
class EndUserRecipe(models.Model):
    enduser=models.ForeignKey(EndUser,on_delete=models.SET_NULL,null=True)
    recipe_name=models.CharField(max_length=30)
    recipe_description=models.CharField(max_length=200)
    # category=models.ForeignKey(RecipeCategory,null=True,on_delete=models.SET_NULL)#either searches for same name field,or considers the primary key of the model
    ingredient_list=models.TextField()
    recipe_procedure=models.TextField()
    no_servings=models.PositiveIntegerField()
    prep_time=models.CharField(max_length=30) #mins/hrs
    cook_time=models.CharField(max_length=30) #mins/hrs
    date_posted=models.DateTimeField(default=django.utils.timezone.now)
    post_type=models.CharField(max_length=20) #public,private
    # def __str__(self): #overriding string method that generally returns the object
    #     return self.recipe_id


class EndUserRecipeImage(models.Model): #a recipe posted by chef/user can have multiple photos
    recipe=models.ForeignKey(EndUserRecipe,on_delete=models.SET_NULL,null=True)
    image=models.ImageField(upload_to='enduser_images/')

class EndUserRecipeLike(models.Model):
    recipe=models.ForeignKey(EndUserRecipe,on_delete=models.SET_NULL,null=True)
    likeduser_type=models.CharField(max_length=20) #chef/user
    likeduser_modeltype=models.ForeignKey(ContentType,on_delete=models.SET_NULL,null=True) #model type could be User/Chef
    likeduser_objectid=models.PositiveIntegerField() #id from the respective model
    likeduser_object=GenericForeignKey('likeduser_modeltype','likeduser_objectid') #like a combo of model type and id 

class EndUserRecipeFeedback(models.Model):
    recipe=models.ForeignKey(EndUserRecipe,on_delete=models.SET_NULL,null=True)
    posteduser_type=models.CharField(max_length=20) #chef/user
    posteduser_modeltype=models.ForeignKey(ContentType,on_delete=models.SET_NULL,null=True) #model type could be User/Chef
    posteduser_objectid=models.PositiveIntegerField() #id from the respective model
    posteduser_object=GenericForeignKey('posteduser_modeltype','posteduser_objectid') #like a combo of model type and id 
    feedback=models.TextField()

class EndUserFollower(models.Model):
    enduser= models.ForeignKey(EndUser,on_delete=models.SET_NULL,null=True)
    follower_type=models.CharField(max_length=20) #either user/chef
    follower_modeltype=models.ForeignKey(ContentType,on_delete=models.SET_NULL,null=True) #model type could be User/Chef
    follower_objectid=models.PositiveIntegerField() #id from the respective model
    follower_object=GenericForeignKey('follower_modeltype','follower_objectid') #like a combo of model type and id 
