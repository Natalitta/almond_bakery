from .models import Booking
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ('booked_item', 'customer', 'number_of_items',
                'personal_message', 'booking_date', 'delivery_time',
                'home_delivery', 'address')
        labels = {
            'booked_item': 'Cake',
            'customer': 'Your Name',
            'number_of_items': 'Number of cakes',
            'personal_message': 'Your personal message 5 &euro;',
            'booking_date': 'Date',
            'delivery_time': 'Preferred Time',
            'home_delivery': 'Delivery 10 &euro;'
        }
        widgets = {
            'booking_date': DateInput(),
        }
