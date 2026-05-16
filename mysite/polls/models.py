from django.db import models

# Create your models here.
class Question(models.Model):
    """ A Question has some text and a publication date. """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    """ A Choice is associated with a Question, and has some text and a vote count. """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)