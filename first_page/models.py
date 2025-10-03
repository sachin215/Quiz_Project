from django.db import models
from django.contrib.auth.models import User




class User_Registry(models.Model):
    Name=models.ForeignKey(User,on_delete=models.CASCADE,related_name='User')
    # Points=models.JSONField(default=list,blank=True, null=True)
    Profile_image=models.ImageField(upload_to='profile_picture',default='default.png')
    
    def __str__(self):
        return self.Name.username

class Score_Board(models.Model):
    User_Registry=models.ForeignKey(User_Registry,on_delete=models.CASCADE,related_name='Score_Board')
    Name=models.CharField(max_length=20)
    Score=models.IntegerField()
    Date=models.DateField(auto_created=True,auto_now_add=True)
    
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published",auto_now_add=True,null=False)
    category=models.CharField(max_length=20,default='Python')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE,related_name='choice',name='choice')
    choice_text =  models.JSONField(default=list)
    answer=models.CharField()
    
    
    def __str__(self):
        return ",".join(self.choice_text)