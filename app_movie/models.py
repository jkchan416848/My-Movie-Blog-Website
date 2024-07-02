from django.db import models

class Movie_Blog_Model(models.Model):
    Movie_Title = models.CharField(max_length=50)
    Movie_Release_date = models.DateField()
    Movie_Review_on = models.DateField()
    Movie_Rating = models.DecimalField(max_digits=2,decimal_places=1)
    Movie_Trailer_link = models.CharField(max_length=1000)
    Movie_Poster = models.ImageField(upload_to='movies_poster')
    Movie_OneLine_Story = models.TextField()
    Movies_Review = models.TextField()
    def __str__(self):
        return self.Movie_Title

class CommentModel(models.Model):
    User_name = models.CharField(max_length=20)
    Movie_name =  models.ForeignKey(Movie_Blog_Model,on_delete=models.CASCADE)
    Comment = models.TextField()
    Rating = models.DecimalField(max_digits=2,decimal_places=1)
    Comment_date = models.DateTimeField(auto_now=True)
    
