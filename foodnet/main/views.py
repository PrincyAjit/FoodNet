from django.shortcuts import render
from django.http import HttpResponse
from .models import RecipeCategory,GeneralRecipe,Appliance
# Create your views here.
def homepage(request):
	return render(request=request,template_name="main/homepage.html")
	
def recipescategories(request):
	return render(request=request,template_name="main/recipecategories.html",context={"categories":RecipeCategory.objects.all(),"count":RecipeCategory.objects.count()})	

def single_slug(request,single_slug):
	recipecategories=[c.category_slug for c in RecipeCategory.objects.all()]
	if single_slug in recipecategories:
		category= RecipeCategory.objects.get(category_slug=single_slug)
		matching_recipes=GeneralRecipe.objects.filter(category__category_slug=single_slug)
		return render(request,"main/recipes.html",context={"recipes":matching_recipes,"category":category})
	# recipes=[a.category_slug for a in GeneralRecipe.objects.all()]
	# if single_slug in recipes:
	# 	return 