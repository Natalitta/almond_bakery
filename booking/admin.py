from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    # Class to view bookings on admin panel
    list_display = (
        'pk',
        'booking_date',
        'booked_item',
        'number_of_items',
        'customer',
        'address',
        'phone',
        'personal_message',
        'completed'
        )
    search_fields = ['pk', 'completed', 'booked_item',
        'booking_date', 'customer__username']
    list_filter = (
        'completed', 'booked_item', 'booking_date'
        )
    actions = ['mark_completed']

    def mark_completed(self, request, queryset):
        queryset.update(completed=True)
