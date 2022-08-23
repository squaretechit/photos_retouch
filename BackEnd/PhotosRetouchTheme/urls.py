from django.urls import path
from . views import SubscriptionEmailView, ContactFormView, ClientReviewView,\
                TeamMemberView, GetQuoteView

urlpatterns = [
    path('client-reviews/', ClientReviewView.as_view(), name='client_reviews'),
    path('our-team/', TeamMemberView.as_view(), name='our_team'),
    path('email/', SubscriptionEmailView.as_view(), name='email'),
    path('quote/', GetQuoteView.as_view(), name='quote'),
    path('contact/', ContactFormView.as_view(), name='contact'),
]
