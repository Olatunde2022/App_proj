from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

# Create your models here.
class Blog(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=True, blank=True, help_text='This section is strictly for tittle')
    body = models.TextField()
    image = models.ImageField(upload_to="media/")  
    rating = models.IntegerField() 
    def __str__(self):
        return f'{self.title} by Ojekab'

class Todo(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, help_text='This is for your title')
    date = models.DateField(auto_now_add=True)
    body = models.TextField()
    scale_of_importance = models.IntegerField()
    def __str__(self):
        return f'{self.title} Powered by: Ojekab'
    
    