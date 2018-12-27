from django.db import models
from .category import  Category
class Product(models.Model):
    prod_name=models.CharField(max_length=50)
    prod_price=models.IntegerField()
    prod_photo=models.ImageField(upload_to='Media/Product_Photo')
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
