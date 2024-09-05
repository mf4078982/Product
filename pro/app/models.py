from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    sku = models.CharField(max_length=50 ,unique=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    supplier = models.CharField(max_length=50)
    
    
def __str__(self):
    return self.name
    