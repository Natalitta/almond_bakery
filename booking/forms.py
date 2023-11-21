from .models import Booking
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = (
            'booked_item', 'phone', 'number_of_items',
            'personal_message', 'booking_date', 'delivery_time',
            'home_delivery', 'address', 'booking_name')
        labels = {
            'booked_item': 'Cake',
            'phone': 'Your contact number',
            'number_of_items': 'Number of cakes',
            'personal_message': 'Your personal message 5 &euro;',
            'booking_date': 'Date',
            'delivery_time': 'Preferred Time',
            'address': 'Address for delivery'
        }
        widgets = {
            'booking_date': DateInput(),
        }
        
        
        def __init__(self, *args, **kwargs):
       
            # Add placeholders, remove auto-generated labels
            super().__init__(*args, **kwargs)
            placeholders = {
                'booking_name': 'Full Name',
                'email': 'Email Address',
                'phone': 'Phone Number',
                'address': 'Full Address',
            }
