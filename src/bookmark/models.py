from django.db import models
from django.contrib.auth.models import User

# Create your models here.
## vo클래스와 유사
class Bookmark(models.Model):
    title = models.CharField('TITLE',max_length=100,blank=True) #오라클의 barchart와 유사 ## verbose_name
    url = models.URLField('URL',unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self): ## 객체표현 양식
        return self.title
