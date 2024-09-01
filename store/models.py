from django.db import models
import datetime

# Create your models here.

class Category(models.Model):
    name= models.CharField(max_length=50)
    
    def __str__(self):     # allows it to be shown in admin 
        return self.name
    
    class Meta:
        verbose_name_plural = 'categories'
    

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email= models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    
    def __str__(self):      
        return f'{self.first_name}{self.last_name}'

class Product(models.Model):
    name = models.CharField(max_length=50)
    price =models.DecimalField(default= 0, decimal_places=2, max_digits=6)
    category = models.ForeignKey(Category, on_delete= models.CASCADE, default=1) #connects it with the Category model
    description = models.CharField(max_length=50, default='', blank=True, null=True) # blank= True makes it so that you can leave blank 
    image =models.ImageField(upload_to='upload/products/') #goes into the media directory
    # Add Sales
    is_sale = models.BooleanField(default=False) # by default, it's not on sale
    sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    
    def __str__(self):     
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE) #ForeignKey connects to Product model
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE) #ForeignKey connects to Customer model
    quantity = models.IntegerField(default=1)
    address= models.CharField(max_length=100, default='', blank=True)
    phone= models.CharField(max_length=30, default='', blank=True)
    date= models.DateField(default=datetime.datetime.today) #used for datetime we imported
    status= models.BooleanField(default=False) #maybe the customer hasn't been delivered yet so false initially
    
    def __str__(self):      
        return self.product
