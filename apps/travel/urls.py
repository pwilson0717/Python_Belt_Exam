from django.conf.urls import url
from . import views

urlpatterns = [

	url(r'^plans$', views.plans, name = "plans"),
	url(r'^add_trip$', views.add_trip, name="add_trip"),
	url(r'^view_plans$', views.add_trip, name="view_plans"),

]