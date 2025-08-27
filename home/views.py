from django.shortcuts import render
from django.http import HttpResponse
from .models import Restaurant

# DRF imports
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import RestaurantSerializer

class MenuView(APIView):
def get(self, request):
# Hardcoded menu data for now
menu = [
{"name": "Margherita Pizza", "description": "Classic cheese and tomato pizza", "price": 8.99},
{"name": "Veggie Burger", "description": "Grilled veggie patty with fresh toppings", "price": 6.49},
{"name": "Pasta Alfredo", "description": "Creamy Alfredo pasta with mushrooms", "price": 7.99},
{"name": "Caesar Salad", "description": "Crisp lettuce with Caesar dressing", "price": 5.99},
]
return Response(menu)
# ---------------- Regular HTML Views ---------------- #
def home(request):
restaurant = Restaurant.objects.first()
restaurant_name = restaurant.name if restaurant else "My Restaurant"
restaurant_phone = restaurant.phone_number if restaurant else "Not Available"

return render(
request,
"home.html",
{
"restaurant_name": restaurant_name,
"restaurant_phone": restaurant_phone,
},
)

def restaurant(request):
return render(request, "restaurant.html")   # restaurant page template

def menu(request):
try:
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

except Exception as e:
return HttpResponse(f"⚠️ Something went wrong while loading the menu: {str(e)}", status=500)

def contact(request):
return render(request, "contact.html")

def reservations(request):
return render(request, "reservations.html")

def feedback_view(request):
if request.method == "POST":
form = FeedbackForm(request.POST)
if form.is_valid():
form.save()
# PRG pattern to avoid duplicate submissions on refresh
return redirect(f"{reverse('feedback')}?submitted=1")
else:
form = FeedbackForm()

submitted = request.GET.get("submitted") == "1"
return render(request, "feedback.html", {"form": form, "submitted": submitted})


# ---------------- REST API Views ---------------- #
@api_view(['GET', 'POST'])
def restaurant_list(request):
if request.method == 'GET':
restaurants = Restaurant.objects.all()
serializer = RestaurantSerializer(restaurants, many=True)
return Response(serializer.data)

elif request.method == 'POST':
serializer = RestaurantSerializer(data=request.data)
if serializer.is_valid():
serializer.save()
return Response(serializer.data, status=status.HTTP_201_CREATED)
return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def restaurant_detail(request, pk):
restaurant = get_object_or_404(Restaurant, pk=pk)

if request.method == 'GET':
serializer = RestaurantSerializer(restaurant)
return Response(serializer.data)

elif request.method == 'PUT':
serializer = RestaurantSerializer(restaurant, data=request.data)
if serializer.is_valid():
serializer.save()
return Response(serializer.data)
return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

elif request.method == 'DELETE':
restaurant.delete()
return Response(
{"message": "Restaurant deleted successfully"},
status=status.HTTP_204_NO_CONTENT
)
