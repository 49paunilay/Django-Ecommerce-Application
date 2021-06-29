from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discounted_price = models.FloatField()
    catagory = models.CharField(max_length=150)
    description = models.TextField()
    size = models.CharField(max_length=5)
    image = models.CharField(max_length=350)
    
    def __str__(self):
        return self.title+" "+self.description
    
class Order(models.Model):
    items = models.CharField(max_length=500)
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    username =models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    totalPrice = models.FloatField()
    
    def __str__(self) -> str:
        return "customer "+self.fname+" "+self.lname

class ContactUs(models.Model):
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    issue = models.TextField()
    
    def __str__(self):
        return self.email + "  with  "+ self.phone + "  has an issue"