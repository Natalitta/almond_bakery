from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    # Class to view bookings on admin panel
    list_display = (
        'pk',
        'customer',
        'booked_item',
        'number_of_items',
        'home_delivery',
        'address',
        'phone',
        'booking_date',
        'delivery_time',
        'completed'
        )
    search_fields = ['pk', 'completed', 'booked_item',
        'booking_date', 'customer__username']
    list_filter = (
        'completed', 'booked_item', 'delivery_time',
        'booking_date', 'home_delivery'
        )
    actions = ['mark_completed']

    def mark_completed(self, request, queryset):
        queryset.update(completed=True)
