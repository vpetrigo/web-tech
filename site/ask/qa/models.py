from django.db import models
from django.contrib.auth.models import User as auth_models_User
from django.db import connection


# Create your models here.
class QuestionManager(models.Manager):
    def new(self):
        data = Question.objects.raw(
            "SELECT * FROM qa_question ORDER BY added_at DESC")

        return data

    def popular(self):
        data = Question.objects.raw(
            "SELECT * FROM qa_question ORDER BY rating DESC")

        return data


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(auth_models_User, on_delete=models.PROTECT)
    likes = models.ManyToManyField(auth_models_User, related_name="likes")
    objects = QuestionManager()

    def __str__(self):
        return "{}".format(self.title)

    class Meta:
        ordering = ["-rating"]


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    author = models.ForeignKey(auth_models_User, on_delete=models.PROTECT)
