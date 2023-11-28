from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import MenuItem, Booking
from .forms import BookingForm
from datetime import timedelta, date
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


class BookingCake(SuccessMessageMixin, CreateView):

    form_class = BookingForm
    template_name = 'booking.html'
    success_url = 'all_bookings'
    success_message = 'Thank you for your order!'
    model = Booking
    

    def post(self, request):
        #booked_item = get_object_or_404(MenuItem, pk=menu_item_id)
        error = ''
        print(request.POST)
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
        if form.is_valid():
            booking = form.save(commit=False)
            booking.customer_id = request.user.id
            booking.save()
            return redirect('all_bookings')
        else:
            error = 'Please check your order'
            return redirect('booking')


class BookingList(LoginRequiredMixin, ListView):
    model = Booking
    queryset = Booking.objects.order_by("booking_date")
    template_name = 'all_bookings.html'


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


class EditBooking(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    form_class = BookingForm
    template_name = 'edit_booking.html'
    success_url = 'all_bookings'
    success_message = 'You have successfully updated your order.'
    model = Booking

    def form_valid(self, form):
        return super(EditBooking, self).form_valid(form)

    def test_func(self):
        return self.request.user


class DeleteBooking(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Booking
    template_name = 'confirm_delete.html'
    success_url = 'all_bookings'
    success_message = 'You have successfully deleted your order.'

    def form_valid(self, form):
        return super(DeleteBooking, self).form_valid(form)

    def test_func(self):
        return self.request.user
