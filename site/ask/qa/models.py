from django.db import models
from django.contrib.auth.models import User as auth_models_User
from django.db import connection

# Create your models here.
class User(auth_models_User):
    pass


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    rating = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    likes = models.ManyToManyField(User, related_name="likes")

    class Meta:
        ordering = ["-rating"]


class QuestionManager(models.Manager):
    def new(self):
        cur = connection.cursor()
        cur.execute("""select * from qa_question
                        order by added_at desc""")

        return cur.fetchall()

    def popular(self):
        cur = connection.cursor()
        cur.execute("""select * from qa_question
                        order by rating desc""")

        return cur.fetchall()


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    author = models.TextField()

