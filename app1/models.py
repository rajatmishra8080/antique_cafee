from django.db import models

# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=100) # the name of the sender
    email = models.EmailField(max_length=254) # the email address of the sender
    message = models.TextField() # the message content

    def __str__(self):
        return self.name