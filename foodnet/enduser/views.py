from django.shortcuts import render,redirect
from django.contrib import messages
from .models import EndUser
# Create your views here.
def afterenduserlogin(request):
	if(request.session['endusername']):
		enduserinfo=EndUser.objects.get(enduser_email=request.session['enduseremail'])
		return render(request=request,template_name="enduser/afterenduserlogin.html",context={"enduserinfo":enduserinfo})
	else:
		return redirect('/')

def logout(request):
	del request.session['endusername']
	del request.session['enduseremail']
	del request.session['type']
	messages.info(request,f"You have been logged out successfully!")
	return redirect('/')