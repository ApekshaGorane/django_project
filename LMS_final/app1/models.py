from django.db import models
from app1.manager import AppManager
# Create your models here.
class BookModel(models.Model):
    book_name=models.CharField(max_length=50)
    author_name=models.CharField(max_length=50)
    price=models.IntegerField()
    page=models.IntegerField()
    type_of_book=models.CharField(max_length=50)
    
    class Meta:
        db_table = 'BookModel'

    obj=AppManager()
