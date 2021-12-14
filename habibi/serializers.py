from rest_framework import serializers
from .models import *


class KiyimlarSerializer(serializers.ModelSerializer):
    class Meta():
        model = Kiyimlar
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    category = KiyimlarSerializer(read_only=True, many=True)
    
    class Meta():
        model = Category
        fields = '__all__'
    
class AloqaSerializer(serializers.ModelSerializer):
    class Meta():
        model = Aloqa
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