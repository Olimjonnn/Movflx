from django.db import models

class Main(models.Model):
    img = models.ImageField(upload_to="Main/")
    link = models.CharField(max_length=255)
    def __str__(self):
        return self.link

class UpcMovies(models.Model):
    img = models.ImageField(upload_to="UpcMovies/")
    name = models.CharField(max_length=200)
    time = models.IntegerField()
    year = models.IntegerField()
    score = models.CharField(max_length=222)
    text = models.TextField()
    link = models.CharField(max_length=250)
    janr = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class BlogMain(models.Model):
    img = models.ImageField(upload_to="blogmain/")

class Blogs(models.Model):
    img = models.ImageField(upload_to="blogs/")
    title = models.CharField(max_length=70)
    text = models.TextField()
    like = models.IntegerField()
    comment = models.IntegerField()
    date = models.DateField()


class Ind(models.Model):
    img = models.ImageField(upload_to="Ind/")
    title = models.CharField(max_length=70)
    text = models.TextField()
    like = models.IntegerField()
    comment = models.IntegerField()
    date = models.DateField()
    link = models.CharField(max_length=250)
    janr = models.CharField(max_length=200)
    time = models.IntegerField()
