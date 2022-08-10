from distutils.command import upload
import email
from django.db import models

# Create your models here.

class book_list(models.Model):
    b_name = models.CharField(max_length=100)
    b_author = models.CharField(max_length=100)
    b_image = models.ImageField(upload_to='pic')
    b_prev = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.b_name
    
class book_comment(models.Model):
    product = models.ForeignKey(book_list,related_name="comments",on_delete=models.CASCADE)
    u_name = models.CharField(max_length=100)
    emi = models.CharField(max_length=100)
    com_area =  models.TextField()
    date = models.DateTimeField(auto_now_add=True)
  