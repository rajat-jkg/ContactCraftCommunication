from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Form(models.Model):
    id = models.AutoField(primary_key=True)
    form_name = models.CharField(max_length=200 , default="Untitled Form")
    form_css = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    sender_name = models.CharField(max_length=200)
    sender_email = models.CharField(max_length=1000)
    sender_phone = models.CharField(max_length=1000,  null=True)
    subject = models.CharField(max_length=1000, null=True)
    message = models.TextField()
    form_id = models.ForeignKey(Form, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)