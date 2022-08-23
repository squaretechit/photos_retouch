from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import UserAdmin

from admin_interface.models import Theme
from rest_framework_simplejwt.tokens import OutstandingToken, BlacklistedToken

from .models import SubscriptionEmail, ContactForm, \
        ClientReview, OurTeam, QuoteForm, QuoteFormImage


admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.unregister(Theme)
admin.site.unregister(OutstandingToken)
admin.site.unregister(BlacklistedToken)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('first_name','last_name','username','email',
                    'is_staff','is_active','date_joined','last_login')
    list_display_links = ('username',)


@admin.register(ClientReview)
class ClientReviewAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'date')
    fields = ('date', 'client_name', 'client_picture', 'review')


@admin.register(OurTeam)
class OurTeamAdmin(admin.ModelAdmin):
    list_display = ('member_name', 'date', 'designation')
    fields = ('date', 'member_name', 'designation', 'picture')


@admin.register(SubscriptionEmail)
class CustomSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'date')


@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('name','email', 'date', 'phone_number')
    fields = ('date', 'name', 'email', 'phone_number', 'comment')


@admin.register(QuoteForm)
class QuoteFormAdmin(admin.ModelAdmin):
    list_display = ('client_name','client_email', 'date')
    fields = ('date', 'client_name', 'client_email', 'filelink', 'services', 'message')
    search_fields = ['client_name', 'client_email']
    list_filter = ['client_name', 'client_email', 'date']


@admin.register(QuoteFormImage)
class QuoteFormImageAdmin(admin.ModelAdmin):
    list_display = ('quote','email', 'date')
    fields = ('date', 'quote', 'email', 'images')
    search_fields = ('email',)
    list_filter = ('date', 'email')
