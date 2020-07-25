from django.db import models

# Create your models here.
class User(models.Model):
    fname=models.CharField(max_length=20)
    lname= models.CharField(max_length=20)
    email= models.CharField(max_length=50)
    username=models.CharField(max_length=30)
    password= models.CharField(max_length=50)


class MovieInfo(models.Model):
    movie_name = models.CharField(max_length=200)
    movie_type = models.CharField(max_length=20)
    movie_review = models.CharField(max_length=20)
    movie_release = models.CharField(max_length=20)
    movie_detail = models.TextField(max_length=500)
    userid = models.ForeignKey(User,on_delete=models.CASCADE)
