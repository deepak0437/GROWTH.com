"""newproject URL Configuration

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
from newApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.homepage_view),
    path('story/', views.storypage_view),
    path('rent/', views.rentalpage_view),
    path('plan/', views.planner_view),
    path('education/', views.educationpage_view),
    path('about/', views.aboutpage_view),
    path('contact/', views.contactpage_view),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', views.logout_view),
    path('signup/', views.signup_view),
    path('store/', views.story_view),
    path('theboy/', views.theboy_view),
    path('thefox/', views.thefox_view),
    path('thegolden/', views.thegolden_view),
    path('theproud/', views.theproud_view),
    path('themilk/', views.themilk_view),
    path('awise/', views.awise_view),
    path('goldenegg/', views.goldenegg_view),
    path('thefarmer/', views.thefarmer_view),
    path('elephant/', views.elephant_view),
    path('niddle/', views.niddle_view),
    path('aglass/', views.aglass_view),
    path('theants/', views.theants_view),
    path('bundle/', views.bundle_view),
    path('thebear/', views.thebear_view),
    path('when/', views.when_view),
    path('miser/', views.miser_view),
    path('thedog/', views.thedog_view),
    path('control/', views.control_view),
    path('theleap/', views.theleap_view),
    path('thewolf/', views.thewolf_view),
    path('gk/', views.gkpage_view),
    path('history/', views.history_view),
    path('geo/', views.geography_view),
    path('sport/', views.sports_view),
    path('eco/', views.economy_view),
    path('test/', views.test_view),
    path('bike/', views.bike_view),
    path('book/', views.bikeone_view)
    
]
