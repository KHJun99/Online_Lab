from django.db import models
import requests

# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length=10)
    author = models.TextField()
    title = models.TextField()
    category_name = models.TextField()
    category_id = models.IntegerField()
    price = models.IntegerField()
    fixed_price = models.BooleanField()
    pub_date = models.DateField()
    
    @classmethod
    def insert_data(cls):
        response = requests.get('http://www.aladin.co.kr/ttb/api/ItemSearch.aspx')
        data = response.json()

        for item in data:
            my_model = cls(field1=item['field1'], field2=item['field2'])
            my_model.save()