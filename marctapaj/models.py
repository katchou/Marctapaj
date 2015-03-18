from django.core.urlresolvers import reverse
from django.utils import timezone
from django.db import models


class Category(models.Model):
	name = models.CharField(max_length = 80)

	def get_absolute_url(self):
		return reverse('marctapaj:index')

	def __str__(self):
		return self.name

class Bookmark(models.Model):
	url = models.URLField()
	name = models.CharField(max_length=80)
	creation_date = models.DateTimeField(auto_now_add=True)
	last_access = models.DateTimeField(auto_now=True)
	access_count = models.IntegerField(default=0, editable=False)
	category = models.ForeignKey(Category)

	def get_absolute_url(self):
		return reverse('marctapaj:index')

	def __str__(self):
		return self.name

class Note(models.Model):
	content = models.TextField()
	update_date = models.DateTimeField(auto_now=True)
	bookmark = models.ForeignKey(Bookmark)

	def get_absolute_url(self):
		return reverse('marctapaj:index')

	def __str__(self):
		return self.content