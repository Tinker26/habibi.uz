from rest_framework import serializers
from .models import *


class KiyimlarSerializer(serializers.ModelSerializer):
    class Meta():
        model = Kiyimlar
        fields = '__all__'
