from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import User, Listing, Reservation, Review, Amenity

# get all users


def user_list(request):
    users = User.objects.all()
    data = {'results': [{'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name,
                         'email': user.email, 'password': user.password, 'is_host': user.is_host} for user in users]}
    return JsonResponse(data)

# get a single user


def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    data = {'id': user.id, 'first_name': user.first_name,
            'last_name': user.last_name, 'email': user.email, 'password': user.password, 'is_host': user.is_host}
    return JsonResponse(data)

# get all listings


def listing_list(request):
    listings = Listing.objects.all()
    data = {'results': [{'id': listing.id, 'owner': listing.owner.id, 'title': listing.title, 'description': listing.description, 'location': listing.location.id,
                         'price_per_night': listing.price_per_night, 'number_of_rooms': listing.number_of_rooms, 'max_guests': listing.max_guests} for listing in listings]}
    return JsonResponse(data)

# get a single listing


def listing_detail(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    data = {'id': listing.id, 'owner': listing.owner.id, 'title': listing.title, 'description': listing.description, 'location': listing.location.id,
            'price_per_night': listing.price_per_night, 'number_of_rooms': listing.number_of_rooms, 'max_guests': listing.max_guests}
    return JsonResponse(data)