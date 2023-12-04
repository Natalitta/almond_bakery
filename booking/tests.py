from django.test import TestCase
from booking.models import Booking


class TestViews(TestCase):

    # Test booking app for logged in user
    def test_setUp(self):
        # Setup test
        username = "Emily"
        password = "emily12345"
        user_model = get_user_model()

        # Create user
        self.user = user_model.objects.create_user(
            username=username,
            password=password,
            is_superuser=False
        )
        logged_in = self.client.login(username=username, password=password)
        self.assertTrue(logged_in)

        # Create booking
        booking = Booking.objects.create(
            customer=self.user,
            booked_item=booked_item,
            number_of_items=1,
            booking_date=date.today(),
            address=address,
            )
