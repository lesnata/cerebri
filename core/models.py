from django.db import models
from django.contrib.auth.models import User

# Create your models here.


LANGUAGE_CHOICES = [
    ('PT', 'Portuguese'),
    ('IT', 'Italian'),
]


class UserProfile(models.User):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @property
    def best_score(self):
        all_scores = self.quiz_set.all()
        quiz_score = [score for score in all_scores]
        return sum(quiz_score)/len(quiz_score)


class Word(models.Model):
    word = models.CharField(max_length=255, blank=False, null=False)
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES)
    translation = models.CharField(max_length=255, null=False)
    date = models.DateTimeField(auto_now_add=True)
    repeated = models.IntegerField(default=0)

    def __str__(self):
        return self.word


class QuizList(models.Model):
    word = models.ForeignKey(Word, on_delete=models.DO_NOTHING)
    answered = models.BooleanField()


class Quiz(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    duration = models.DurationField()
    quiz_list = models.ForeignKey(QuizList, on_delete=models.DO_NOTHING)

    @property
    def score(self):
        quiz_list_words = self.quizlist_set.all()
        correct_answers = len([item for item in quiz_list_words if item.answered])
        return correct_answers












