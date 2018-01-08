from django import forms
from .models import director,movie,leadactors
from django.forms import Select

class userform(forms.ModelForm):
    # name= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Movie Name'}))
    # genre= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Movie Genre'}))
    # release_date = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','placeholder':'Release Date'}))
    # actors = forms.ModelMultipleChoiceField(queryset=leadactors.objects.all(),widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Actor Name'}))
    class Meta:
        model=movie
        fields=['name','genre','release_date','director','actors']
        #exclude=('actors',)
        #widgets={ 'actors':Select(),}
    #actors=forms.ModelMultipleChoiceField(queryset=leadactors.objects.all())

    #fields='__all__'
        #exclude=['name','actors','release_date','genre','director']
    # CHOICES= [
    # ('orange', 'Oranges'),
    # ('cantaloupe', 'Cantaloupes'),
    # ('mango', 'Mangoes'),
    # ('honeydew', 'Honeydews'),
    # ]
    # Movie_name=forms.CharField(max_length=100)
    # Movie_genre=forms.CharField(max_length=100)
    # Actor=forms.CharField(label="Select actor",widget=forms.Select(choices=CHOICES))
