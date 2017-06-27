from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from .models import Plans, Schedules
from ..login.models import Users

def plans(request):
	if "login_id" in request.session:
		print "this is the dashboard **********"
		context = {
			"user_name": Users.objects.get(id = request.session["login_id"]),
		}
		return render(request, "travel/plans.html", context)
	else:
		return redirect(reverse("login:index"))

def add_trip(request):	
	if "login_id" in request.session:
		context = {
			"all_trips": Plans.objects.all(),
		}
		return render(request, "travel/addTrip.html")
	else:
		return redirect(reverse("travel:plans"))

def view_plans(request):
	if "login_id" in request.session:
		context = {
			"all_users": Users.objects.all(),
			"all_plans": Plans.objects.all(),
			"all_schedules": Schedules.objects.all(),
		}
		return render(request, "travel/plans.html", context)
	else:
		return redirect(reverse("login:index"))



