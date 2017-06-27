from __future__ import unicode_literals

from django.db import models
from ..login.models import Users

class PlansManager(models.Manager):
	def add(self, destination, description, start_date, end_date):
		errors = []

		if len(postData["destination"]) < 5:
			errors.append("The destination field is required.")
		if len(postData["description"]) < 5:
			errors.append("The description field is required.")
		if len(postData["start_date"]) < 0:
			errors.append("The Travel Date From field is required.")
		if len(postData["end_date"]) < 0:
			errors.append("The Travel Date To field is required.")

		if postData["end_date"] < postData[start_date]:
			errors.append("The Travel To date can not be before the Travel From date.")

		if len(errors):
			return{
				"status": False,
				"errors": errors
			}
		else:
			return {
				"status": True,
				"user_name": self.create(
					destination = postData["destination"],
					description = postData["description"],
					start_date = postData["start_date"],
					end_date = postData["end_date"],
					)
			}

class Plans(models.Model):
	user_name = models.ForeignKey(Users)
	destination = models.CharField(max_length=255)
	description = models.TextField()
	start_date = models.DateField()
	end_date = models.DateField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = PlansManager()

class SchedulesManager(models.Manager):
	def add(self, plan, destination, start_date, end_date):
		return {
		"user_name": self.create(
			plan = postData["plan"],
			destination = postData["destination"],
			start_date = postData["start_date"],
			end_date = postData["end_date"],
			)
		}

class Schedules(models.Model):
	user_name = models.ForeignKey(Users)
	plan = models.CharField(max_length=255)
	destination = models.ForeignKey(Plans, related_name="travel_destination")
	start_date = models.ForeignKey(Plans, related_name="start")
	end_date = models.ForeignKey(Plans, related_name="end")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

