from django.db import models
import uuid
import os

def user_profile_image_upload_path(instance, filename):
    ext = filename.split('.')[-1]  # Extract file extension
    new_filename = f"{uuid.uuid4()}.{ext}"  # Generate unique filename using UUID
    return os.path.join('profile_images/', new_filename)

class UserProfile(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)
    project_links = models.TextField()
    description = models.TextField()
    profile_image = models.ImageField(upload_to=user_profile_image_upload_path, blank=True, null=True)

    def __str__(self):
        return self.username
