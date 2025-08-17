from django.shortcuts import render
from .models import Restaurant


def home(request):
    restaurant = Restaurant.objects.first()
    restaurant_name = restaurant.name if restaurant else "My Restaurant"
    return render(request, "home.html", {"restaurant_name": restaurant_name})

def restaurant(request):
    return render(request, "restaurant.html")   # restaurant page template

def menu(request):
    menu_items = [
    {'name': 'Butter Chicken', 'price': 275},
    {'name': 'Paneer Butter Masala', 'price': 250},
    {'name': 'Veg Manchuria', 'price': 150},
    
    # Biryani
    {'name': 'Hyderabadi Chicken Biryani', 'price': 210},
    {'name': 'Paneer Biryani', 'price': 185},
    ]
    
    context = {'menu_items': menu_items}
    return render(request, 'menu.html', context)