from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers

from .models import SubscriptionEmail, ContactForm, ClientReview, OurTeam


class ClientReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientReview
        fields = '__all__'


class OurTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurTeam
        fields = '__all__'


class SubscriptionEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionEmail
        fields = ('email',)


class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = ('name', 'email', 'phone_number', 'comment')
