from django.db import models
from django.contrib import auth

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateField(auto_now=True, auto_now_add=True)
    rating = models.IntegerField()
    author = models.ForeignKey("User", to_field="username", on_delete=models.PROTECT)
    likes = models.ManyToManyField("User")


class QuestionManager(models.Manager):
    def new(self):
        pass

    def popular(self):
        pass


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(auto_now=True, auto_now_add=True)
    question = models.ForeignKey("Question", on_delete=models.PROTECT)
    author = models.TextField()


class User(auth.models.User):
    pass

