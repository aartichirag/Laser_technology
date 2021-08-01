from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MinValueValidator

# Create your models here.
class product_info(models.Model):
    product_name=models.CharField(max_length=50)
    product_qty=models.IntegerField(validators=[MinValueValidator(0,"Quntity should not be negative")])
    description=models.TextField()
    price=models.IntegerField(validators=[MinValueValidator(0,"price should not be negative")])
    category=models.ForeignKey('category.category_master',on_delete=models.PROTECT,related_name='product_info')

    def __str__(self):
        return f" {self.product_name}-{self.category}"

    def get_absolute_url(self):
        return reverse('product-view')