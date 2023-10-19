from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class CategoryType(models.Model):
    name=models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class Location(models.Model):
    name=models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
# class Product(models.Model):
#     name=models.CharField(max_length=255)
#     quantity=models.IntegerField()
#     contact=models.CharField(max_length=255)
#     image=models.ImageField(null=True)
#     category=models.ForeignKey(Category, on_delete=models.PROTECT,null=True)
#     categorytype=models.ForeignKey(CategoryType, on_delete=models.PROTECT,null=True)
#     location=models.ForeignKey(Location, on_delete=models.PROTECT,null=True)
    
#     def __str__(self):
#         return self.name

class MombasaProduct(models.Model):
    seller=models.CharField(max_length=255)
    quantity=models.IntegerField()
    contact=models.CharField(max_length=255)
    color=models.CharField(max_length=255,null=True)
    image=models.ImageField(upload_to='images/')
    category=models.ForeignKey(Category, on_delete=models.PROTECT,null=True)
    categorytype=models.ForeignKey(CategoryType, on_delete=models.PROTECT,null=True)
    location=models.ForeignKey(Location, on_delete=models.PROTECT,null=True)
    
class KwaleProduct(models.Model):
    seller=models.CharField(max_length=255)
    quantity=models.IntegerField()
    contact=models.CharField(max_length=255)
    color=models.CharField(max_length=255,null=True)
    image=models.ImageField(null=True)
    category=models.ForeignKey(Category, on_delete=models.PROTECT,null=True)
    categorytype=models.ForeignKey(CategoryType, on_delete=models.PROTECT,null=True)
    location=models.ForeignKey(Location, on_delete=models.PROTECT,null=True)
   
    def __str__(self) -> str:
        return super().__str__()
    
class LamuProduct(models.Model):
    seller=models.CharField(max_length=255)
    quantity=models.IntegerField()
    contact=models.CharField(max_length=255)
    color=models.CharField(max_length=255,null=True)
    image=models.ImageField(null=True)
    category=models.ForeignKey(Category, on_delete=models.PROTECT,null=True)
    categorytype=models.ForeignKey(CategoryType, on_delete=models.PROTECT,null=True)
    location=models.ForeignKey(Location, on_delete=models.PROTECT,null=True)
    
    def __str__(self) -> str:
        return super().__str__()
    
class TanaRiverProduct(models.Model):
    seller=models.CharField(max_length=255)
    quantity=models.IntegerField()
    contact=models.CharField(max_length=255)
    color=models.CharField(max_length=255,null=True)
    image=models.ImageField(null=True)
    category=models.ForeignKey(Category, on_delete=models.PROTECT,null=True)
    categorytype=models.ForeignKey(CategoryType, on_delete=models.PROTECT,null=True)
    location=models.ForeignKey(Location, on_delete=models.PROTECT,null=True)
    
    def __str__(self) -> str:
        return super().__str__()
    
class KilifiProduct(models.Model):
    seller=models.CharField(max_length=255)
    quantity=models.IntegerField()
    contact=models.CharField(max_length=255)
    color=models.CharField(max_length=255,null=True)
    image=models.ImageField(null=True)
    category=models.ForeignKey(Category, on_delete=models.PROTECT,null=True)
    categorytype=models.ForeignKey(CategoryType, on_delete=models.PROTECT,null=True)
    location=models.ForeignKey(Location, on_delete=models.PROTECT,null=True)
    
    def __str__(self) -> str:
        return super().__str__()