from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from analytics.models import View
from .models import BlogPost


class BlogListView(ListView):
	model = BlogPost


class BlogDetailView(DetailView):
	model = BlogPost

	def get_object(self):
		post_pk = self.kwargs.get("pk") # grab the primary key of the object
		post_query = BlogPost.objects.filter(pk=post_pk) # returns a list with the filtered results
		if post_query.exists():
			post_object = post_query.first() # grab the first item in the list if it exists
			view, created = View.objects.get_or_create(
						user=self.request.user,
						post=post_object
					) # specify the fields for the View object to be created
			if view:
				view.views_count += 1 # add 1 view onto the view tally
				view.save()
			return post_object
		raise Http404 # if the object does not exist




