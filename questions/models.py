from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



# Create your models here.


class Questions(models.Model):
    user = models.ForeignKey(User,related_name='Questions_author', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=50000)
    created_at = models.DateTimeField(default=timezone.now)


    
    def __str__(self):
        return self.title
    

class Answer(models.Model):
    user = models.ForeignKey(User,related_name='comment_author',on_delete=models.CASCADE)
    questions = models.ForeignKey(Questions , related_name='Answer_Questions', on_delete=models.CASCADE)
    answer = models.TextField(max_length=500)
    create_at = models.DateTimeField(default= timezone.now)
