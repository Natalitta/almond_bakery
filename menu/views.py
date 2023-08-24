from django.shortcuts import render, get_object_or_404
from django.views import generic, View
# from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import MenuItem
# from .forms import BookingForm
from datetime import timedelta, date
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages


class MenuList(generic.ListView):
    model = MenuItem
    queryset = MenuItem.objects.order_by("title")
    template_name = "index.html"
