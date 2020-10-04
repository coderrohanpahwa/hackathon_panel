from django.db import models
class Contact(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    query=models.TextField()
    def __str__(self):
        return self.name
class Scoreboard(models.Model):
    name=models.CharField(max_length=20,null=True)
    username=models.CharField(max_length=20)
    score=models.IntegerField(null=True)
    answer=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Answer(models.Model):
    name=models.CharField(max_length=100,null=True)
    answer=models.CharField(max_length=100,null=True)
    username=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.name