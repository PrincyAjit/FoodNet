from django.shortcuts import render
from django.http import HttpResponse
from .models import RecipeCategory,GeneralRecipe,Appliance,ApplianceCategory
# Create your views here.
def homepage(request):
	return render(request=request,template_name="main/homepage.html")

def about(request):
	return render(request=request, template_name="main/about.html")

def contact(request):
	return render(request=request, template_name="main/contact.html")
	
def recipescategories(request):
	return render(request=request,template_name="main/recipecategories.html",context={"categories":RecipeCategory.objects.all(),"count":RecipeCategory.objects.count()})	


def appliancecategories(request):
	return render(request=request,template_name="main/appliancecategories.html", context={'categories':ApplianceCategory.objects.all(), "count":ApplianceCategory.objects.count()} )

def single_slug(request,single_slug):
	recipecategories=[c.category_slug for c in RecipeCategory.objects.all()]
	if single_slug in recipecategories:
		category= RecipeCategory.objects.get(category_slug=single_slug)
		matching_recipes=GeneralRecipe.objects.filter(category__category_slug=single_slug)
		return render(request,"main/recipes.html",context={"recipes":matching_recipes,"category":category})
	
	appliancecategories=[c.category_slug for c in ApplianceCategory.objects.all()] #bakingAppliances, all
	if single_slug in appliancecategories:
		category= ApplianceCategory.objects.get(category_slug=single_slug)
		matching_appliances=Appliance.objects.filter(appliance_category__category_slug=single_slug) #bakingAppliances == bakingAppliances
		return render(request,"main/appliances.html",context={"appliances":matching_appliances, "category":category})
        
    