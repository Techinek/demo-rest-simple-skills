from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.CharField(max_length=10)
    author = models.ForeignKey(to=Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title
