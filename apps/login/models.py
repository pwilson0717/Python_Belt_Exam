from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

def get_pw_hash(pw, salt = bcrypt.gensalt()):
	return(bcrypt.hashpw(pw, salt))


class UsersManager(models.Manager):
	def register(self, postData):
		errors = []

		if len(postData["name"]) < 1:
			errors.append("The name field is empty.")

		if len(postData["user_name"]) < 1:
			errors.append("Your user name is required.")

		if len(postData["pw_1"]) < 1:
			errors.append("Your password is required.")
		elif len(postData["pw_1"]) < 8:
			errors.append("Your password must be at least 8 characters.")
		elif not re.match(r'^.*[A-Z]+.*$', postData['pw_1'] ):
			errors.append("The password must contain at least 1 capital letter.")
		elif not re.match(r'^.*\d+.*$', postData['pw_1']):
			errors.append("The password must contain at least 1 number.")

		if postData["pw_1"] != postData["pw_2"]:
			errors.append("The passwords do not match.")

		if len(errors):
			return {
				"status": False,
				"errors": errors
			}
		else:
			return {
				"status": True,
				"user": self.create(
					name = postData["name"],
					user_name = postData["user_name"],
					password = get_pw_hash(postData["pw_1"].encode()),
					)
			}

	def login(self, postData):
		errors = []

		if len(postData["pw"]) < 1:
			errors.append("Your password is required.")
		else:
			user = self.get(user_name = postData["user_name"])
			if get_pw_hash(postData["pw"].encode(), user.password.encode()) != user.password:
				errors.append("Incorrect password.")

		if len (errors):
			return {
				"status": False,
				"errors": errors
			}
		else:
			return {
				"status": True,
				"user": self.get(user_name = postData["user_name"])
			}

class Users(models.Model):
	name = models.CharField(max_length = 255)
	user_name = models.CharField(max_length = 255)
	password = models.CharField(max_length = 50)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	objects = UsersManager()

