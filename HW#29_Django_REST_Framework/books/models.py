from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    year = models.DateField()
    price = models.FloatField(null=True)
    rating = models.FloatField(null=True)
    authors = models.ManyToManyField(Author)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title
