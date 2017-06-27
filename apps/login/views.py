from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from .models import Users

def index(request):

		return render(request, "login/index.html")

def register(request):
	if request.method == "POST":
		print "this is a log in ***************"
		db_result = Users.objects.register(request.POST)
		if not db_result["status"]:
			print "not status***************"
			messages.add_message(request, messages.INFO, "Attempt to register failed.")
			for i in db_result["errors"]:
				messages.add_message(request, messages.INFO, "- " + i)
			return redirect(reverse("login:index"))
		else:
			print "this is else!!***************"
			request.session["login_id"] = db_result["user"].id
			request.session["name"] = db_result["user"].name
			request.session["user_name"] = db_result["user"].user_name
			request.session["new_registration"] = 1
			return redirect(reverse("travel:index"))
	else:
		return redirect(reverse("login:index"))

def login(request):
	if request.method == "POST":
		print "this is a log in **************"
		db_result = Users.objects.login(request.POST)
		if not db_result["status"]:
			messages.add_message(request, messages.INFO, "Login failed.")
			for i in db_result["errors"]:
				messages.add_message(request, messages.INFO, "- " + i)
			return redirect(reverse("login:index"))
		else:
			print "Can you find me???????????"
			request.session["login_id"] = db_result["user"].id
			request.session["user_name"] = db_result["user"].user_name
			return redirect(reverse("travel:plans"))
	# else:
	# 	print "what about me??????????*******"
	# 	return redirect(reverse("login:index"))

def logout(request):
	request.session.clear()
	return redirect(reverse("login:index"))
