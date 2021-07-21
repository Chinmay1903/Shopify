from django.db import models

# Create your models here.


class product(models.Model):
    productname = models.CharField(max_length=60)
    category = models.CharField(max_length=60)
    subcategory = models.CharField(max_length=60)
    description = models.CharField(max_length=6000)
    images = models.CharField(max_length=6000)
    price = models.CharField(max_length=60)

    def __str__(self):
        return self.productname
