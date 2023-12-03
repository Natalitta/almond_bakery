from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import MenuItem


class MenuList(generic.ListView):
    # View all menu items
    model = MenuItem
    queryset = MenuItem.objects.order_by("title")
    template_name = "index.html"
