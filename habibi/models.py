from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Kiyimlar(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    content = models.TextField(default="")
    image = models.ImageField()
    size = models.IntegerField(default=0)
    number = models.IntegerField(default=0)
    category = models.ForeignKey('Category', related_name="category", on_delete=models.PROTECT)

    class Meta():
        verbose_name = 'Kiyim'
        verbose_name_plural = 'Kiyimlar'
        ordering = ['name']

    def __str__(self):
        return self.name 
        
class Category(models.Model):
    name = models.CharField(max_length=300)

    class Meta():
        ordering = ['name']
    
    class Meta():
        verbose_name = 'Categorya'
        verbose_name_plural = 'Categoryalar'
        ordering = ['name']

    def __str__(self):
        return self.name 

class Aloqa(models.Model):
    name = models.CharField(max_length=100)
    Email = models.EmailField()
    subject = models.CharField(max_length=300)
    massage = models.TextField(default=0)
    
    class Meta():
        ordering = ['name']
    
    class Meta():
        verbose_name = 'Aloqa'
        verbose_name_plural = 'Aloqalar'
        ordering = ['name']

    def __str__(self):
        return self.name 

class Card(models.Model):
    user = models.ForeignKey(get_user_model(), related_name="cards", on_delete=models.PROTECT, default=None)   
    is_sold = models.BooleanField(default=False)
    added_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.user.username}: {self.added_date}"

class CardItem(models.Model):
    product = models.ForeignKey(Kiyimlar, related_name="carditems", on_delete=models.PROTECT, default=None)
    total = models.IntegerField(default=1)
    card = models.ForeignKey(Card, related_name="carditems",on_delete=models.CASCADE, default=None)

    def __str__(self) -> str:
        return self.product.name