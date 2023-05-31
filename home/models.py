from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class EmailList(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    subject = models.CharField(max_length=100, null=True)
    attachment = models.FileField(upload_to='media', null=True)
    email_body = models.TextField(null=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name