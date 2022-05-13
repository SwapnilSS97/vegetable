from django.db import models
class Fruits(models.Model):
    fruitname=models.CharField(max_length=20)
    fruitprice=models.FloatField()
    fruitstock=models.IntegerField()
    fruitimage=models.CharField(max_length=100)
    class Meta:
        db_table="fruits"

# Create your models here.
