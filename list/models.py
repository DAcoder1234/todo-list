from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings  # Import settings to reference AUTH_USER_MODEL

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  # Ensure email is unique
    username = models.CharField(max_length=150, blank=True, null=True)  # Not required

    USERNAME_FIELD = 'email'  # Login with email instead of username
    REQUIRED_FIELDS = []  # No additional fields required

class Todo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Reference dynamic user model
    value=models.FloatField(default=5)
    order=models.FloatField( default=0)
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    priority=models.IntegerField(null=True)
    try:
        deadline= models.DateField(null=True)
    except:
        pass
    
    def __str__(self):
        
        return self.title
        
