from django import forms
from .models import Vote


class VotingForm(forms.Form):
    chosen_books_options = forms.MultipleChoiceField(choices=[], label='Book Name', required=False,
                                                     widget=forms.SelectMultiple(
                                                        attrs={
                                                             'class': 'form-control'
                                                         }
                                                     ))
    other_book_name = forms.CharField(label='Other', max_length=100, required=False,
                                      widget=forms.TextInput(
                                        attrs={
                                              'class': 'form-control',
                                              'placeholder': 'Did we miss something?'
                                          }
                                      ))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        unique_books_names = Vote.objects.order_by('book_name').values_list('book_name', flat=True).distinct()
        self.fields['chosen_books_options'].choices = [(book_name, book_name) for book_name in unique_books_names]
