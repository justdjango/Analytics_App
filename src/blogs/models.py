from django.db import models

# Create your models here.

class BlogPost(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField()


	def __str__(self):
		return self.title # display the object by its title