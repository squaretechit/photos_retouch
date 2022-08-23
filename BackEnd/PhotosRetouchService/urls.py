from django.urls import path
from . views import ServiceView, ServiceCalculator, SingleServiceSlider, SinglePortfolio, ServiceGallerie

urlpatterns = [
    path('service/', ServiceView.as_view(), name='service'),
    path('calculator/', ServiceCalculator.as_view(), name='service'),
    path('service-sliders/', SingleServiceSlider.as_view(), name='service_slider'),
    path('service-portfolio/', SinglePortfolio.as_view(), name='service_portfolio'),
    path('service-gallery/', ServiceGallerie.as_view(), name='service_gallery'),
]
