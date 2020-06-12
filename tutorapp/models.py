from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models he




class Profile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=25,blank=True)
    university = models.CharField(max_length=25,blank=True)
    college = models.CharField(max_length=25,blank=True)
    school = models.CharField(max_length=25,blank=True)
    address = models.CharField(max_length=100,blank=True)
    role = models.CharField(max_length=25,blank=True)
    gender = models.CharField(max_length=25,blank=True)
   

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()


    
class Post(models.Model):
    category = models.CharField(max_length=25)
    clas = models.CharField(max_length=25)
    subject = models.CharField(max_length=100)
    city = models.CharField(max_length=100)     
    place = models.CharField(max_length=100)
    place_detail = models.CharField(max_length=100)
    gender = models.CharField(max_length=25)
    no_student = models.IntegerField()
    salary = models.IntegerField()
    title = models.CharField(max_length=100)
    phone = models.IntegerField()