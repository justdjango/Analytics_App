from django.http import JsonResponse
from django.shortcuts import render

from .models import View

def analytics_view(request):
	context = {
		'views': 10
	}
	return JsonResponse(context)