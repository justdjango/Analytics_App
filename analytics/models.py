from django.conf import settings
from django.db import models

from blogs.models import BlogPost
# Create your models here.

class View(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	post = models.OneToOneField(BlogPost)
	views_count = models.IntegerField(default=0)

	def __str__(self):
		return "{}-{}".format(self.post, self.views_count)