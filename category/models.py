from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class category_master(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse('category-view')

