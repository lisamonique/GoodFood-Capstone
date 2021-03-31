from datetime import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    veggie_question = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.veggie_question

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="vegetable_questions")
    veggie_answer = models.BooleanField(default=True)

    def __str__(self):
        return self.veggie_answer
