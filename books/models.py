from django.conf import settings
from django.db import models
from django.utils import timezone

class Book(models.Model):
	author = models.CharField(max_length=200)
	title = models.CharField(max_length=200)
	book_notes = models.TextField(blank=True, null=True)
	put_on_shelf_date = models.DateTimeField(default=timezone.now)
	start_date = models.DateTimeField(blank=True, null=True)
	end_date = models.DateTimeField(blank=True, null=True)
	status = models.CharField(max_length=200)
	genre = models.CharField(max_length=200)
	rating = models.FloatField(blank=True, null=True)

	def put_on_shelf(self):
		self.save()

	def __str__(self):
		return self.title
