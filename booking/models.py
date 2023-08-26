from django.db import models
from menu.models import MenuItem
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Choice fields
DELIVERY_TIME = ((1, "morning"), (2, "afternoon"), (3, "evening"))


class Booking(models.Model):

    # Model for making bookings of menu items
    customer = models.ForeignKey(User, on_delete=models.CASCADE,
        related_name="booking_customer")
    booking_name = models.CharField(max_length=25)
    booked_item = models.ForeignKey(MenuItem,
        on_delete=models.CASCADE, related_name="ordered_item")
    number_of_items = models.IntegerField(default=1)
    personal_message = models.TextField(blank=True, max_length=100)
    booking_date = models.DateField()
    home_delivery = models.BooleanField(default=False)
    address = models.CharField(max_length=100)
    delivery_time = models.IntegerField(choices=DELIVERY_TIME, default=1)
    completed = models.BooleanField(default=False)

    class Meta:
        # Order by booking_date and booking_time
        ordering = ['booking_date', 'delivery_time']

    def __str__(self):
        return str(self.pk)
