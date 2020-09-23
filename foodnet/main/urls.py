"""foodnet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .import views
app_name="main"
urlpatterns = [
	path("activate/<uidb64>/<token>",
        views.activate_account, name='activate'),
    path("",views.homepage,name="homepage"),
    path("recipescategories",views.recipescategories,name="recipescategories"),
    path("login",views.login,name="login"),
    path("signup",views.signup,name="signup"),
    path("<single_slug>",views.single_slug,name="single_slug"),
    # path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
