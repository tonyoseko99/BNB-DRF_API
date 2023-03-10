import json
import requests
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.shortcuts import get_object_or_404


from rest_framework.parsers import JSONParser

from django.views.generic import UpdateView, DeleteView
from django.views.decorators.csrf import csrf_exempt


from .serializers import UserSerializer, ListingSerializer, ReservationSerializer, ReviewSerializer, AmenitySerializer, ListingAmenitySerializer
from .models import User, Listing, Reservation, Review, Amenity, ListingAmenity


# create a user


@csrf_exempt
def user_create(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

# get all users


def user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)

    return JsonResponse({"users": serializer.data}, safe=False)

# get a single user and show their listings


def user_detail(request, pk):
    user = User.objects.get(pk=pk)
    serializer = UserSerializer(user)
    return JsonResponse(serializer.data, safe=False)

# update a user


@csrf_exempt
# update a user using UpdateView
def user_update(request, pk):
    if request.method == 'PATCH':
        data = JSONParser().parse(request)
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)


# delete a user

@csrf_exempt
def user_delete(request, pk):
    if request.method == 'DELETE':
        user = User.objects.get(pk=pk)
        user.delete()
        return JsonResponse({"message": "user deleted successfully"}, status=200)
    return JsonResponse({"message": "Invalid request method"}, status=405)

# create a listing


@csrf_exempt
def listing_create(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ListingSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201,)
        return JsonResponse(serializer.errors, status=400)


# get all listings


def listing_list(request):
    listings = Listing.objects.all()
    serializer = ListingSerializer(listings, many=True)

    return JsonResponse({'listings': serializer.data}, status=200)


# get a single listing


def listing_detail(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    listing_serializer = ListingSerializer(listing)
    user_serializer = UserSerializer(listing)

    return JsonResponse({'listing': listing_serializer.data}, status=200)


# update a listing


@csrf_exempt
def listing_update(request, pk):
    if request.method == 'PATCH':
        data = JSONParser().parse(request)
        listing = Listing.objects.get(pk=pk)
        serializer = ListingSerializer(listing, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)


# delete a listing

@csrf_exempt
def listing_delete(request, pk):
    if request.method == 'DELETE':
        listing = Listing.objects.get(pk=pk)
        listing.delete()
        return JsonResponse({"message": "listing deleted successfully"}, status=200)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

# create a reservation


@csrf_exempt
def create_reservation(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ReservationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

# get all reservations


def reservation_list(request):
    reservations = Reservation.objects.all()
    serializer = ReservationSerializer(reservations, many=True)

    return JsonResponse({'reservations': serializer.data}, status=200)

# get a single reservation


def reservation_detail(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    serializer = ReservationSerializer(reservation)

    return JsonResponse(serializer.data)

# update a reservation


@csrf_exempt
def reservation_update(request, pk):
    if request.method == 'PATCH':
        data = JSONParser().parse(request)
        reservation = Reservation.objects.get(pk=pk)
        serializer = ReservationSerializer(
            reservation, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message": "Reservation updated successfully"}, status=200)
        return JsonResponse(serializer.errors, status=400)

# delete a reservation


@csrf_exempt
def reservation_delete(request, pk):
    if request.method == 'DELETE':
        reservation = Reservation.objects.get(pk=pk)
        reservation.delete()
        return JsonResponse({"message": "Reservation deleted successfully"}, status=200)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

# create a review


def create_review(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ReviewSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


# get all reviews


def review_list(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)

    return JsonResponse({'reviews': serializer.data}, status=200)

# get a single review


def review_detail(request, pk):
    review = get_object_or_404(Review, pk=pk)
    serializer = ReviewSerializer(review)

    return JsonResponse(serializer.data)

# update a review


def review_update(request, pk):
    if request.method == 'PATCH':
        data = JSONParser().parse(request)
        review = Review.objects.get(pk=pk)
        serializer = ReviewSerializer(review, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message": "Review updated successfully"}, status=200)
        return JsonResponse(serializer.errors, status=400)

# delete a review


def review_delete(request, pk):
    if request.method == 'DELETE':
        review = Review.objects.get(pk=pk)
        review.delete()
        return JsonResponse({"message": "Review deleted successfully"}, status=200)
    return JsonResponse({'error': 'Invalid request method'}, status=405)


# create an Amenity

def create_amenity(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AmenitySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

# get all amenities


def amenity_list(request):
    amenities = Amenity.objects.all()
    serializer = AmenitySerializer(amenities, many=True)

    return JsonResponse({'amenities': serializer.data}, status=200)

# get a single amenity


def amenity_detail(request, pk):
    amenity = get_object_or_404(Amenity, pk=pk)
    serializer = AmenitySerializer(amenity)

    return JsonResponse(serializer.data)


# update an amenity


def amenity_update(request, pk):
    if request.method == 'PATCH':
        data = JSONParser().parse(request)
        amenity = Amenity.objects.get(pk=pk)
        serializer = AmenitySerializer(amenity, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message": "Amenity updated successfully"}, status=200)
        return JsonResponse(serializer.errors, status=400)

# delete an amenity


def amenity_delete(request, pk):
    if request.method == 'DELETE':
        amenity = Amenity.objects.get(pk=pk)
        amenity.delete()
        return JsonResponse({"message": "Amenity deleted successfully"}, status=200)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

# create Amenities for a listing


def create_listing_amenity(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ListingAmenitySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

# get all listing amenities


def listing_amenity_list(request):
    listing_amenities = ListingAmenity.objects.all()
    serializer = ListingAmenitySerializer(listing_amenities, many=True)

    return JsonResponse({'listing_amenities': serializer.data}, status=200)

# get a single listing amenity


def listing_amenity_detail(request, pk):
    listing_amenity = get_object_or_404(ListingAmenity, pk=pk)
    serializer = ListingAmenitySerializer(listing_amenity)

    return JsonResponse(serializer.data)

# update a listing amenity


def listing_amenity_update(request, pk):
    if request.method == 'PATCH':
        data = JSONParser().parse(request)
        listing_amenity = ListingAmenity.objects.get(pk=pk)
        serializer = ListingAmenitySerializer(
            listing_amenity, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message": "Listing amenity updated successfully"}, status=200)
        return JsonResponse(serializer.errors, status=400)


# delete a listing amenity


def listing_amenity_delete(request, pk):
    if request.method == 'DELETE':
        listing_amenity = ListingAmenity.objects.get(pk=pk)
        listing_amenity.delete()
        return JsonResponse({"message": "Listing amenity deleted successfully"}, status=200)
    return JsonResponse({'error': 'Invalid request method'}, status=405)


# # create a location


# def create_location(request):
#     data = {}
#     data['name'] = request.POST.get('name')
#     data['listings'] = request.POST.get('listings')
#     location = Location.objects.create(**data)
#     data['id'] = location.id
#     return JsonResponse(data)

# # get all locations


# def location_list(request):
#     locations = Location.objects.all()
#     data = {'results': [{'id': location.id, 'name': location.name, 'listings': location.listings}
#                         for location in locations]}
#     return JsonResponse(data)

# # get a single location


# def location_detail(request, pk):
#     location = get_object_or_404(Location, pk=pk)
#     data = {'id': location.id, 'name': location.name,
#             'listings': location.listings}
#     return JsonResponse(data)

# # update a location


# class LocationUpdate(LoginRequiredMixin, UpdateView):
#     model = Location
#     fields = ['name', 'listings']

#     def get_object(self, queryset=None):
#         location_id = self.kwargs.get('pk')
#         return Location.objects.get(id=location_id)

# # delete a location


# class LocationDelete(LoginRequiredMixin, DeleteView):
#     model = Location

#     def get_object(self, queryset=None):
#         location_id = self.kwargs.get('pk')
#         return Location.objects.get(id=location_id)

#     def delete_location(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         self.object.delete()
#         return JsonResponse({"message": "Location deleted successfully"})
