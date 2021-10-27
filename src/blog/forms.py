'''
Created on 2021. 8. 12.
FormView할때 forms만듦
@author: pc358
'''
from django import forms

class PostSearchForm(forms.Form):
    search_word = forms.CharField(label = '찾는단어')