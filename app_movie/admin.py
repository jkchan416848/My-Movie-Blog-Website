from django.contrib import admin
from .models import Movie_Blog_Model,CommentModel

# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ['User_name','Movie_name','Comment','Rating','Comment_date']



admin.site.register(Movie_Blog_Model)
admin.site.register(CommentModel,CommentAdmin)
