from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from newApp.forms import SignForm
from django.http import HttpResponseRedirect


# Create your views here.
def homepage_view(request):
    return render(request,'newApp/home.html')
def storypage_view(request):
    return render(request,'newApp/story.html')
def story_view(request):
    return render(request,'newApp/store.html')
def theboy_view(request):
    return render(request,'newApp/theboy.html')
def thegolden_view(request):
    return render(request,'newApp/thegolden.html')
def thefox_view(request):
    return render(request,'newApp/thefox.html')
def theproud_view(request):
    return render(request,'newApp/theproud.html')
def themilk_view(request):
    return render(request,'newApp/themilk.html')
def awise_view(request):
    return render(request,'newApp/awise.html')
def goldenegg_view(request):
    return render(request,'newApp/goldenegg.html')
def thefarmer_view(request):
    return render(request,'newApp/thefarmer.html')
def elephant_view(request):
    return render(request,'newApp/elephant.html')
def when_view(request):
    return render(request,'newApp/when.html')
def rentalpage_view(request):
    return render(request,'newApp/rent.html')
def thebear_view(request):
    return render(request,'newApp/thebear.html')
def niddle_view(request):
    return render(request,'newApp/niddle.html')
def aglass_view(request):
    return render(request,'newApp/aglass.html')
def theants_view(request):
    return render(request,'newApp/theants.html')
def bundle_view(request):
    return render(request,'newApp/bundle.html')
def miser_view(request):
    return render(request,'newApp/miser.html')
def thedog_view(request):
    return render(request,'newApp/thedog.html')
def control_view(request):
    return render(request,'newApp/control.html')
def theleap_view(request):
    return render(request,'newApp/theleap.html')
def thewolf_view(request):
    return render(request,'newApp/thewolf.html')
def gkpage_view(request):
    return render(request,'newApp/gk.html')
def educationpage_view(request):
    return render(request,'newApp/education.html')
def history_view(request):
    return render(request,'newApp/history.html')
def geography_view(request):
    return render(request,'newApp/geo.html')
def sports_view(request):
    return render(request,'newApp/sport.html')
def test_view(request):
    return render(request,'newApp/test.html')
def economy_view(request):
    return render(request,'newApp/economy.html')
def planner_view(request):
    return render(request,'newApp/planner.html')
def aboutpage_view(request):
    return render(request,'newApp/about.html')
def contactpage_view(request):
    return render(request,'newApp/contact.html')
def logout_view(request):
    return render(request,'newApp/logout.html')
def bike_view(request):
    return render(request,'newApp/bike.html')
def bikeone_view(request):
    return render(request,'newApp/bikeone.html')
def signup_view(request):
    form=SignForm()
    if request.method=='POST':
        form=SignForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'newApp/signup.html',{'form':form})
