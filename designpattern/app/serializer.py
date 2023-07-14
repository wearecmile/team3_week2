from rest_framework import serializers
from .models import Car, CarModel

class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ['id', 'brand', 'color', 'size']

class CarModelSerializer(serializers.ModelSerializer):
    car_brand_detail = CarSerializer(source='car_id')

    class Meta:
        model = CarModel
        fields = ['id', 'car_model_id', 'car_name', 'car_brand_detail', 'car_details']