from . import views
from django.urls import path

urlpatterns = [
    path('create/', views.BookingCake.as_view(), name='booking'),
    path('all_bookings/', views.BookingList.as_view(), name='all_bookings'),
    path('edit/<slug:pk>/', views.EditBooking.as_view(), name='edit_booking'),
    path('delete/<slug:pk>/', views.DeleteBooking.as_view(), name='confirm_delete'),
]
