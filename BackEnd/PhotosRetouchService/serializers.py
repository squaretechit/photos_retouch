from rest_framework import serializers

from .models import Service, ServiceCalculator, ServiceSlider, ServicePortfolio, ServiceGallerie


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class ServiceCalculatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCalculator
        fields = '__all__'


class ServiceSliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceSlider
        fields = '__all__'


class ServicePortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicePortfolio
        fields = '__all__'


class ServiceGallerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceGallerie
        fields = '__all__'
