from django.db import models
from main.models import RecipeCategory
from enduser.models import EndUser
import datetime,django
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# Create your models here.
class Chef(models.Model):
    chef_name=models.CharField(max_length=30)
    chef_email=models.EmailField(unique=True)
    date_joined=models.DateTimeField(default=django.utils.timezone.now)
    chef_password=models.CharField(max_length=15)
    chef_dob=models.DateField(default=datetime.date.today)
    chef_photo=models.ImageField()
    chef_bio=models.TextField(default="-")
    validation_counts=models.PositiveIntegerField(default=0) #no of recipes they have validated
    # def __str__(self):#overriding string method that generally returns the object
    #     return self.chef_id


class ChefExpertiseArea(models.Model):
    chef=models.ForeignKey(Chef,null=True,on_delete=models.SET_NULL) #CASCADE is to delete the entry if the corresponding foreign key entry is deleted
    expertise=models.ForeignKey(RecipeCategory,null=True,on_delete=models.SET_NULL) #based on category,can select upto 3


class ChefDoc(models.Model):
    chef=models.ForeignKey(Chef,null=True,on_delete=models.SET_NULL,verbose_name="Chef id") #cascade deletes the entry if the corresponding referenced value is deleted
    doc=models.FileField(unique=True)



class Event(models.Model):
    event=models.AutoField(primary_key=True,default=0)
    event_name=models.CharField(max_length=50)
    event_description=models.TextField()
    event_datetime=models.DateTimeField()
    event_duration=models.CharField(max_length=30,default=0)
    event_type=models.CharField(max_length=20) #free/paid
    event_amount=models.PositiveIntegerField(default=0) #if 0,then free event
    chef_id=models.ForeignKey(Chef,null=True,on_delete=models.SET_NULL,verbose_name="Chef id")
    # def __str__(self): #overriding string method that generally returns the object
    #     return self.event_id



class EventRegistration(models.Model):
    event=models.ForeignKey(Event,on_delete=models.CASCADE)
    reguser_type=models.CharField(max_length=20) #chef/user
    reguser_modeltype=models.ForeignKey(ContentType,on_delete=models.SET_NULL,null=True) #model type could be User/Chef
    reguser_objectid=models.PositiveIntegerField(default=0) #id from the respective model
    reguser_object=GenericForeignKey('reguser_modeltype','reguser_objectid') #like a combo of model type and id 
    # def __str__(self): #overriding string method that generally returns the object
    #     return self.reg_id



class ChefRecipe(models.Model):
    chef=models.ForeignKey(Chef,on_delete=models.SET_NULL,null=True)
    recipe_name=models.CharField(max_length=30)
    recipe_description=models.CharField(max_length=200)
    category=models.ForeignKey(RecipeCategory,null=True,on_delete=models.SET_NULL) #either searches for same name field,or considers the primary key of the model
    ingredient_list=models.TextField()
    recipe_procedure=models.TextField()
    no_servings=models.PositiveIntegerField(default=0)
    prep_time=models.CharField(max_length=30) #mins/hrs
    cook_time=models.CharField(max_length=30) #mins/hrs
    date_posted=models.DateTimeField(default=django.utils.timezone.now)
    post_type=models.CharField(max_length=20) #public,private
    # def __str__(self): #overriding string method that generally returns the object
    #     return self.recipe_id


class ChefRecipeImage(models.Model): #a recipe posted by chef/user can have multiple photos
    recipe=models.ForeignKey(ChefRecipe,on_delete=models.SET_NULL,null=True)
    image=models.ImageField()

class ChefRecipeLike(models.Model):
    recipe=models.ForeignKey(ChefRecipe,on_delete=models.SET_NULL,null=True)
    likeduser_type=models.CharField(max_length=20) #chef/user
    likeduser_modeltype=models.ForeignKey(ContentType,on_delete=models.SET_NULL,null=True) #model type could be User/Chef
    likeduser_objectid=models.PositiveIntegerField() #id from the respective model
    likeduser_object=GenericForeignKey('likeduser_modeltype','likeduser_objectid') #like a combo of model type and id 

class ChefRecipeFeedback(models.Model):
    recipe=models.ForeignKey(ChefRecipe,on_delete=models.SET_NULL,null=True)
    posteduser_type=models.CharField(max_length=20) #chef/user
    posteduser_modeltype=models.ForeignKey(ContentType,on_delete=models.SET_NULL,null=True) #model type could be User/Chef
    posteduser_objectid=models.PositiveIntegerField() #id from the respective model
    posteduser_object=GenericForeignKey('posteduser_modeltype','posteduser_objectid') #like a combo of model type and id 
    feedback=models.TextField()

class UserRecipesValidation(models.Model):
    recipe=models.ForeignKey(EndUser,on_delete=models.SET_NULL,null=True) #foreign key to user recipe table
    chef=models.ForeignKey(Chef,null=True,on_delete=models.SET_NULL)
    status=models.CharField(max_length=20) #validated,notvalidated

class ChefFollower(models.Model):
    chef= models.ForeignKey(Chef,on_delete=models.SET_NULL,null=True)
    follower_type=models.CharField(max_length=20) #either user/chef
    follower_modeltype=models.ForeignKey(ContentType,on_delete=models.SET_NULL,null=True) #model type could be User/Chef
    follower_objectid=models.PositiveIntegerField() #id from the respective model
    follower_object=GenericForeignKey('follower_modeltype','follower_objectid') #like a combo of model type and id 




