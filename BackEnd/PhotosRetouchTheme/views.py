from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings

from rest_framework import generics
from rest_framework.response import Response

from .models import SubscriptionEmail, ContactForm, ClientReview, OurTeam, QuoteForm, QuoteFormImage
from .serializers import SubscriptionEmailSerializer, ContactFormSerializer, ClientReviewSerializer, OurTeamSerializer


class ClientReviewView(generics.RetrieveAPIView):
    queryset = ClientReview.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ClientReviewSerializer(queryset, many=True)
        return Response(serializer.data)


class TeamMemberView(generics.RetrieveAPIView):
    queryset = OurTeam.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = OurTeamSerializer(queryset, many=True)
        return Response(serializer.data)


class SubscriptionEmailView(generics.RetrieveAPIView):
    queryset = SubscriptionEmail.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = SubscriptionEmailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'You are successfully Subscribed.'})


class GetQuoteView(generics.RetrieveAPIView):

    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            if data['filelink']:
                CreateQuote = QuoteForm(
                    client_name= data['name'],
                    client_email= data['email'],
                    services= data['services_list'],
                    message= data['message'],
                    filelink= data['filelink']
                )
                CreateQuote.save()
        except:
            CreateQuote = QuoteForm(
                client_name= data['name'],
                client_email= data['email'],
                services= data['services_list'],
                message= data['message']
            )
            CreateQuote.save()
            all_images = request.FILES.getlist('images')
            for image in all_images:
                qoute_image = QuoteFormImage(
                    quote=CreateQuote,
                    email= data['email'],
                    images = image
                )
                qoute_image.save()
        return Response({'message': 'Your request is accepted. Admin will contact you soon.'})


class ContactFormView(generics.RetrieveAPIView):
    queryset = ContactForm.objects.all()

    def post(self, request, format=None):
        serializer = ContactFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            name = request.data['name']
            email = request.data['email']
            phone_number = request.data['phone_number']
            comment = request.data['comment']
            mail = f'''Hi Admin,
I am {name},
My Email {email},
My Phone Number {phone_number},
My Message: {comment}'''
            send_mail(
                f"Message from {get_current_site(request).domain}",
                mail,
                settings.EMAIL_HOST_USER,
                settings.ADMIN_EMAIL_FOR_NOTIFICATIONS,
                fail_silently=False,)
            return Response({'message': 'We will contact you soon.'})
