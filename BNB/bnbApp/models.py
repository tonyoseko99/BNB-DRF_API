from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    is_host = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
