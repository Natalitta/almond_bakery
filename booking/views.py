from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import MenuItem, Booking
from .forms import BookingForm
from datetime import timedelta, date
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages


class BookingCake(LoginRequiredMixin, CreateView):

    form_class = BookingForm
    template_name = 'booking.html'
    success_url = 'all_bookings'
    model = Booking

    # def form_valid(self, form):
    #    return super(BookingCake, self).form_valid(form)

    def order(request):
        error = ''
        data = {
            'form': form,
            'error': error
        }

        if request.method == POST:
            form = BookingForm(request.post)
            if form.is_valid():
                form.instance.customer = self.request.user
                form.save()
                return redirect('all_bookings.html')
            else:
                error = 'Please check your order'


class BookingList(LoginRequiredMixin, ListView):
    model = Booking
    queryset = Booking.objects.order_by("booking_date")
    template_name = 'all_bookings.html'


class EditBooking(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    form_class = BookingForm
    template_name = 'edit_booking.html'
    success_url = "all_bookings"
    model = Booking

    def form_valid(self, form):
        messages.success(
            self.request,
            f'You have successfully updated your order.'
        )
        return super(EditBooking, self).form_valid(form)

    def test_func(self):
        return self.request.user


class DeleteBooking(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Booking
    template_name = 'confirm_delete.html'
    success_url = "all_bookings"

    def form_valid(self, form):
        messages.success(
            self.request,
            'You have successfully deleted your order'
        )
        return super(DeleteBooking, self).form_valid(form)
