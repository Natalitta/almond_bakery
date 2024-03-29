from .models import Booking
from django import forms
from datetime import date, timedelta


class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = (
            'booked_item', 'phone', 'number_of_items',
            'personal_message', 'booking_date', 'address', 'booking_name')
        labels = {
            'booked_item': 'Cake',
            'phone': 'Your phone number e.g. +3531234567',
            'number_of_items': 'Number of cakes',
            'personal_message': 'Your personal message 5 &euro;',
            'booking_date': 'Date',
            'address': 'Address for delivery'
        }
        widgets = {
            'booking_date': DateInput(
                attrs={'min': date.today() + timedelta(days=1)}
                ),
        }
