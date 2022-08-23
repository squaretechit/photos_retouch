from rest_framework import generics
from rest_framework.response import Response

from .models import Service, ServiceCalculator, ServiceSlider, ServicePortfolio, ServiceGallerie
from .serializers import ServiceSerializer, ServiceCalculatorSerializer, ServiceSliderSerializer, \
                    ServicePortfolioSerializer, ServiceGallerieSerializer


class ServiceView(generics.RetrieveAPIView):
    queryset = Service.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ServiceSerializer(queryset, many=True)
        return Response(serializer.data)


class ServiceCalculator(generics.RetrieveAPIView):
    queryset = ServiceCalculator.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ServiceCalculatorSerializer(queryset, many=True)
        return Response(serializer.data)


class SingleServiceSlider(generics.RetrieveAPIView):
    queryset = ServiceSlider.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ServiceSliderSerializer(queryset, many=True)
        return Response(serializer.data)


class SinglePortfolio(generics.RetrieveAPIView):
    queryset = ServicePortfolio.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ServicePortfolioSerializer(queryset, many=True)
        return Response(serializer.data)


class ServiceGallerie(generics.RetrieveAPIView):
    queryset = ServiceGallerie.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ServiceGallerieSerializer(queryset, many=True)
        return Response(serializer.data)
