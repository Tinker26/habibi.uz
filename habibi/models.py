from django.db import models

# Create your models here.
class Kiyimlar(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    content = models.TextField(default="")
    image = models.ImageField()
    size = models.IntegerField(default=0)
    number = models.IntegerField(default=0)

    

    class Meta():
        verbose_name = 'Kiyim'
        verbose_name_plural = 'Kiyimlar'
        ordering = ['name']

    def __str__(self):
        return self.name 
        