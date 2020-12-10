from cloudinary.models import CloudinaryField
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models

class Member(AbstractUser):
    phone_number = models.CharField(blank=True, max_length=15)
    role = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Member {self.id} | {self.username}"

class Visitor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    date_filled = models.DateTimeField(auto_now=True)

    adults_count = models.IntegerField(default=1)
    children_count = models.IntegerField(default=0)

    def __str__(self):
        return f"Visitor {self.id} | {self.email}"

class Child(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    father = models.ForeignKey(Member, on_delete=models.CASCADE, blank=True, related_name='fathers_children')
    mother = models.ForeignKey(Member, on_delete=models.CASCADE, blank=True, related_name='mothers_children')
    guardian = models.ForeignKey(Member, on_delete=models.CASCADE, blank=True, related_name='guardians_children')

    def __str__(self):
        return f"Child {self.id} | {self.first_name} {self.last_name}"

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
