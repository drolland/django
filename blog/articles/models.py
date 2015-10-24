from django.db import models


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200,null=True)
    author = models.CharField(max_length=200)
    date = models.DateTimeField('Date Published')
    text = models.TextField()

    def __str__(self):
        return self.title + " - " + self.author