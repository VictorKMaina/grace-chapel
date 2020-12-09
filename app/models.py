from cloudinary.models import CloudinaryField
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models

class Member(AbstractUser):
    phone_number = models.CharField(blank=True, max_length=15)
    role = models.CharField(max_length=255, blank=True)

class Visitor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    date_visited = models.DateTimeField(auto_now_add=True)

    friends_count = models.IntegerField()
    children_count = models.IntegerField()

class Child(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    father = models.ForeignKey(Member, on_delete=models.CASCADE, blank=True, related_name='fathers_children')
    mother = models.ForeignKey(Member, on_delete=models.CASCADE, blank=True, related_name='mothers_children')
    guardian = models.ForeignKey(Member, on_delete=models.CASCADE, blank=True, related_name='guardians_children')

    def clean(self):
        cleaned_data = super().clean()
        if not cleaned_data.get('father') and not cleaned_data.get('mother') and not cleaned_data.get('guardian'):
            raise ValidationError('You have to specify a father, mother, or guardian.')

class Sermon(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=350)
    preacher = models.ForeignKey(Member, on_delete=models.CASCADE)
    video_path = CloudinaryField()
    thumbnail_path = CloudinaryField()
    date_created = models.DateTimeField(auto_now_add=True)
