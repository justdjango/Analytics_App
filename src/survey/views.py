from django.shortcuts import render

from .forms import VotingForm
from .models import Vote


def index(request):
    if request.method == 'POST':
        form = VotingForm(request.POST)
        if form.is_valid():
            chosen_books_options = form.cleaned_data.get('chosen_books_options', [])
            other_book_name = form.cleaned_data.get('other_book_name', '')
            Vote.bulk_vote(chosen_books_options + [other_book_name])
        message = 'Thank You For Your Contribution!'
    elif request.method == 'GET':
        message = ''

    form = VotingForm()
    return render(request, 'templates/survey.html', {'form': form, 'message': message})
