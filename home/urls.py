from django.urls import path
from . import views
from .views import MenuView

urlpatterns = [
    path("", views.home, name="restaurant_home"),
    path('menu/', views.menu, name='menu'),
    path("contact/", views.contact, name="contact"),
    path('', include('feedback.urls')),
    path('api/menu/', MenuView.as_view(), name='menu'),
]