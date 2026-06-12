from django.db import models

class Activity(models.Model):
    name = models.CharField(max_length=200)
    time = models.TimeField()
    trigger = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Command(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name="commands")
    command_text = models.CharField(max_length=255)
    response_text = models.TextField()

    def __str__(self):
        return self.command_text


class LanguageGuide(models.Model):
    letter = models.CharField(max_length=1)
    code_word = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.letter} - {self.code_word}"


class QuizQuestion(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question


class Score(models.Model):
    username = models.CharField(max_length=100)
    score = models.IntegerField(default=0)
    
    