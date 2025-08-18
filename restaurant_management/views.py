from django.shortcuts import render

def restaurant_page(request):
    return render(request, 'restaurant.html')