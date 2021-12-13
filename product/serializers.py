from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta():
        model = Product
        fields = '__all__'

class ProductCategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(read_only=True, many=True)
    class Meta():
        model = Categorya
        fields = '__all__'
        
class CardItemSerializer(serializers.ModelSerializer):    

    class Meta():
        model = CardItem
        fields = '__all__'
 
class CardSerializer(serializers.ModelSerializer):    
    carditems = CardItemSerializer(read_only=True, many=True)
    class Meta():
        model = Card
        fields = '__all__'