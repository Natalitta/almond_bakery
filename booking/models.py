from django.db import models
from menu.models import MenuItem
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from phonenumber_field.modelfields import PhoneNumberField


class Booking(models.Model):

    # Model for making bookings of menu items
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="booking_customer")
    booking_name = models.CharField(max_length=25)
    phone = PhoneNumberField(blank=False)
    booked_item = models.ForeignKey(
        MenuItem, on_delete=models.CASCADE, related_name="ordered_item")
    number_of_items = models.IntegerField(default=1)
    personal_message = models.CharField(blank=True, max_length=100)
    booking_date = models.DateField()
    address = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)

    class Meta:
        # Order by booking_date
        ordering = ['booking_date']

    def __str__(self):
        return str(self.booked_item)
