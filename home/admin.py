from django.contrib import admin
from .models import Restaurant 

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    # At least one option should be inside the class
    list_display = ('name','phone_number')   # shows the restaurant name in the admin table