from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token 
# Create your models here.


class Kota(models.Model):
    kota=models.CharField(max_length=500)
    def __str__(self):
        return '%s' % (self.kota)

class Leveluser(models.Model):
    level=models.CharField(max_length=20)    

    def __str__(self):
        return '%s' % (self.level)


class User(AbstractUser):
    nama=models.CharField(max_length=300)
    tgl=models.CharField(max_length=300,blank=True,null=True)
    alamatlengkap=models.TextField()
    email=models.EmailField(max_length=200,unique=True)
    username=models.CharField(max_length=300,unique=True)
    password=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now_add=True, blank=True,null=True)
    leveluser=models.ForeignKey(Leveluser,on_delete=models.CASCADE,null=True, default="1")
    kota=models.ForeignKey(Kota,on_delete=models.CASCADE,null=True,blank=True)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    
    def __str__(self):
        return '%s %s %s %s %s %s %s %s' % (self.nama,self.kota,self.date,self.tgl,self.leveluser,self.email,self.username,self.alamatlengkap)

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, on_delete=models.CASCADE, related_name='replies',blank=True)
    
    class Meta:
        ordering = ["-created_date"]
    
    def __str__(self):
        return '%s' % (self.created_date,self.parent,self.post,self.text)



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)