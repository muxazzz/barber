from django.contrib import admin
from barber.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    @staticmethod
    def author_full_name(obj):
        return obj.author.full_name
    list_display = ('client_name', 'client_email',)
    fields = ('client_email', 'client_tel', 'client_comments', 'client_city','client_name', 'client_order')
# Register your models here.
