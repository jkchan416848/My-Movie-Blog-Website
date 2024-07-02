from django import forms
from .models import Movie_Blog_Model,CommentModel

class Movie_Blog_form(forms.ModelForm):
    class Meta:
        model = Movie_Blog_Model
        fields = "__all__"
        widgets = {'Movie_Release_date':forms.DateInput(attrs={'type':'date'}),
                  'Movie_Review_on':forms.DateInput(attrs={'type':'date'}),
                  'Movie_Trailer_link':forms.Textarea(attrs={'width':'1280px','height':'720px'})}      
        
class Comment_form(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = "__all__"
        widgets =  {'Movie_name':forms.HiddenInput,'User_name':forms.HiddenInput}       