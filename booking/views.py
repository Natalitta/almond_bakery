from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import MenuItem, Booking
from .forms import BookingForm
from datetime import timedelta, date
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy


class BookingCake(LoginRequiredMixin,SuccessMessageMixin, CreateView):
    # Make a booking
    form_class = BookingForm
    template_name = 'booking.html'
    success_url = 'all_bookings'
    success_message = 'Thank you for your order!'
    model = Booking

    def post(self, request):
        # Post booking form
        error = ''
        form_data = {
            'booking_name': request.POST['booking_name'],
            'phone': request.POST['phone'],
            'address': request.POST['address'],
            'booked_item': request.POST['booked_item'],
            'number_of_items': request.POST['number_of_items'],
            'personal_message': request.POST['personal_message'],
            'booking_date': request.POST['booking_date'],
        }
        form = BookingForm(form_data)
        form.instance.customer = self.request.user

        if form.is_valid():
            booking = form.save(commit=False)
            booking.save()
            return super(BookingCake, self).form_valid(form)
        else:
            error = 'Please check your order'
            return render(request, self.template_name, {'form': form, 'error': error})


class BookingList(LoginRequiredMixin, ListView):
    # View all bookings of a user
    model = Booking
    template_name = 'all_bookings.html'

    def get_queryset(self):
        return Booking.objects.filter(
            customer=self.request.user).order_by("booking_date")


class SuccessMessageMixin:
    # Add a message if form submitted successfully.
    success_message = ''

    def form_valid(self, form):
        response = super().form_valid(form)
        success_message = self.get_success_message(form.cleaned_data)
        if success_message:
            messages.success(self.request, success_message)
        return response

    def get_success_message(self, cleaned_data):
        return self.success_message % cleaned_data


class EditBooking(
                SuccessMessageMixin, LoginRequiredMixin,
                UserPassesTestMixin, UpdateView):
    # Edit booking
    form_class = BookingForm
    template_name = 'edit_booking.html'
    success_url = 'all_bookings'
    success_message = 'You have successfully updated your order.'
    model = Booking

    def form_valid(self, form):
        form.save()
        return redirect('all_bookings')

    def test_func(self):
        return self.request.user


class DeleteBooking(
                    SuccessMessageMixin, LoginRequiredMixin,
                    UserPassesTestMixin, DeleteView):
    # Delete booking and confirm deletion
    model = Booking
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('all_bookings')
    success_message = 'You have successfully deleted your order.'

    def form_valid(self, form):
        return super(DeleteBooking,self).form_valid(form)

    def test_func(self):
        return self.request.user
