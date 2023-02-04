from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import User, Listing, Reservation, Review, Amenity

# get all users


def user_list(request):
    users = User.objects.all()
    data = {'results': [{'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name,
                         'email': user.email, 'password': user.password, 'is_host': user.is_host} for user in users]}
