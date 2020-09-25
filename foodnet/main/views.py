from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import RecipeCategory,GeneralRecipe,Appliance, ApplianceCategory
from enduser.models import EndUser
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .token_generator import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.urls import reverse
import django,datetime
import logging
from django.core.files.storage import FileSystemStorage
logger = logging.getLogger("mylogger")

# Create your views here.
def homepage(request):
	return render(request=request,template_name="main/homepage.html")
	
def recipescategories(request):
	return render(request=request,template_name="main/recipecategories.html",context={"categories":RecipeCategory.objects.all(),"count":RecipeCategory.objects.count()})	
def about(request):
	return render(request=request, template_name="main/about.html")

def contact(request):
	return render(request=request, template_name="main/contact.html")
	
def appliancecategories(request):
	return render(request=request,template_name="main/appliancecategories.html", context={'categories':ApplianceCategory.objects.all(), "count":ApplianceCategory.objects.count()} )

def signup(request):
	if request.method=='POST':
		signuptype=request.POST['signup_type']
		if(signuptype=="enduser"):
			if (EndUser.objects.filter(enduser_email=request.POST['email'],is_active=True).exists()):
				messages.info(request,f"An account exists with this email,signup with another account")
				return render(request=request,template_name="main/signup.html",context={"type":signuptype})
			else:	
				encryptedpassword=make_password(request.POST['password'],"a")
				photo=request.FILES['userphoto']
				logger.info(photo)
				fs=FileSystemStorage()
				filename=fs.save(photo.name,photo)
				photo_url=fs.url(filename)
				photo_url=photo_url[7:]  #removing the media word getting attached,as that is already done by MEDIA_URL
				logger.info(photo_url)
				enduser=EndUser(enduser_name=request.POST['name'],enduser_email=request.POST['email'],enduser_dob=request.POST['dob'],enduser_password=encryptedpassword,enduser_photo=photo_url,enduser_bio=request.POST['bio'])
				enduser.is_active=False
				enduser.save()
				emailid=request.POST['email']
				domain = get_current_site(request).domain
				uidb64=urlsafe_base64_encode(force_bytes(enduser.pk))
				token=account_activation_token.make_token(enduser)
				link=reverse('main:activate',kwargs={'uidb64':uidb64,'token':token})
				domain=domain[:-1]
				logger.info(domain)
				logger.info(uidb64)	
				logger.info(token)
				logger.info(link)
				activate_url='http://'+domain+link
				logger.info(activate_url)
				email_body='Hi '+enduser.enduser_name+' Please use this link to verify your account\n'+activate_url	
				email_subject='Activate your account'
				email = EmailMessage(email_subject,email_body,to=[emailid])
				a=email.send()
				if(a!=0):
					messages.info(request,f"We have sent you an email,please click on the link in it to activate your account.")
					return redirect('/')	
		elif(signuptype=="chef"):
			messages.info(request,f"Signup type is chef,not yet done!")
			return redirect('/')
	else:
		signuptype=request.GET.get('signup_type')
		return render(request=request,template_name="main/signup.html",context={"type":signuptype})

def activate_account(request, uidb64, token):
	try:
		uid = force_bytes(urlsafe_base64_decode(uidb64))
		user = EndUser.objects.get(pk=uid)
	except(TypeError, ValueError, OverflowError, EndUser.DoesNotExist):
		user = None
	if user is not None and account_activation_token.check_token(user, token):
		user.is_active = True
		user.save()
		messages.info(request,f"Your account has been activated successfully!login to continue")
		return redirect('/')
	else:
		messages.info(request,f"Activation link is invalid!")
		return redirect('/')

def login(request):
	if request.method=='POST':
		logintype=request.POST['login_type']
		if(logintype=="enduser"):
			encryptedpassword=make_password(request.POST['password'],"a")
			logger.info(encryptedpassword)
			if EndUser.objects.filter(enduser_email=request.POST['email'],enduser_password=encryptedpassword,is_active=True).exists():
					request.session['endusername'] = EndUser.objects.get(enduser_email=request.POST['email'],enduser_password=encryptedpassword).enduser_name
					request.session['enduseremail'] = EndUser.objects.get(enduser_email=request.POST['email'],enduser_password=encryptedpassword).enduser_email
					request.session['type'] = 'enduser'
					messages.success(request,f"Logged in successfully")
					enduserinfo=EndUser.objects.get(enduser_email=request.POST['email'])
					return render(request=request,template_name="enduser/afterenduserlogin.html",context={"enduserinfo":enduserinfo})
			else:
				messages.error(request,f"User does not exist.Please give valid credentials")
				return redirect('/')
		elif(logintype=="chef"):
			messages.info(request,f"Login type is chef.Not done yet!")
			return redirect('/')

	else:		
		logintype=request.GET.get('login_type')
		return render(request=request,template_name="main/login.html",context={"type":logintype})

def single_slug(request,single_slug):
	recipecategories=[c.category_slug for c in RecipeCategory.objects.all()]
	if single_slug in recipecategories:
		category= RecipeCategory.objects.get(category_slug=single_slug)
		matching_recipes=GeneralRecipe.objects.filter(category__category_slug=single_slug)
		return render(request,"main/recipes.html",context={"recipes":matching_recipes,"category":category})
	recipe=[a.recipe_slug for a in GeneralRecipe.objects.all()]
	if single_slug in recipe:
		recipeinfo= GeneralRecipe.objects.get(recipe_slug=single_slug)
		return render(request,"main/recipe.html",context={"recipe":recipeinfo})
	appliancecategories=[c.category_slug for c in ApplianceCategory.objects.all()] #bakingAppliances, all
	if single_slug in appliancecategories:
		category= ApplianceCategory.objects.get(category_slug=single_slug)
		matching_appliances=Appliance.objects.filter(appliance_category__category_slug=single_slug) #bakingAppliances == bakingAppliances
		return render(request,"main/appliances.html",context={"appliances":matching_appliances, "category":category})

