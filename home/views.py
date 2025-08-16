from django.shortcuts import render
from .models import Restaurant


def home(request):
    restaurant = Restaurant.objects.first()
    restaurant_name = restaurant.name if restaurant else "My Restaurant"
    return render(request, "home.html", {"restaurant_name": restaurant_name})

def restaurant(request):
    return render(request, "restaurant.html")   # restaurant page template
