from __future__ import unicode_literals

from django.db import models

class User(models.Model):
	name = models.CharField(max_length=50)
	branch = models.CharField(max_length=30)
	year = models.CharField(max_length=5)
	phone = models.CharField(max_length=15)
	email = models.EmailField()

	def __unicode__(self):
		return self.name

class Feedback(models.Model):
	title = models.CharField(max_length=30, blank=True, null=True)
	feedback = models.TextField()

	def __unicode__(self):
		return self.title+ ' | '+self.feedback

class Team(models.Model):
	name = models.CharField(max_length=30)
	branch = models.CharField(max_length=50)
	phone = models.CharField(max_length=15)
	email = models.EmailField()

	def __unicode__(self):
		return self.name