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


from .serializers import UserSerializer, ListingSerializer, ReservationSerializer, ReviewSerializer, AmenitySerializer
from .models import User, Listing, Reservation, Review, Amenity, ListingAmenity


def home_view(request):
    return JsonResponse({'message': 'Welcome to the BnB API'})
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

# get a single user


def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    serializer = UserSerializer(user)

    return JsonResponse(serializer.data)

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
    serializer = ListingSerializer(listing)

    return JsonResponse(serializer.data)

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
    data = {'reservations': [{'id': reservation.id, 'listing': reservation.listing.id, 'guest': reservation.guest.id, 'start_date': reservation.start_date, 'end_date': reservation.end_date,
                              'number_of_guests': reservation.number_of_guests, 'total_price': reservation.total_price} for reservation in reservations]}
    return JsonResponse(data)

# get a single reservation


def reservation_detail(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    data = {'id': reservation.id, 'listing': reservation.listing.id, 'guest': reservation.guest.id, 'start_date': reservation.start_date, 'end_date': reservation.end_date,
            'number_of_guests': reservation.number_of_guests, 'total_price': reservation.total_price}
    return JsonResponse(data)

# update a reservation


class ReservationUpdate(LoginRequiredMixin, UpdateView):
    model = Reservation
    fields = ['listing', 'guest', 'start_date', 'end_date',
              'number_of_guests', 'total_price']

    def get_object(self, queryset=None):
        reservation_id = self.kwargs.get('pk')
        return Reservation.objects.get(id=reservation_id)

# delete a reservation


class ReservationDelete(LoginRequiredMixin, DeleteView):
    model = Reservation

    def get_object(self, queryset=None):
        reservation_id = self.kwargs.get('pk')
        return Reservation.objects.get(id=reservation_id)

    def deleteReservation(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return JsonResponse({"message": "Reservation deleted successfully"})

# create a review


def create_review(request):
    data = {}
    data['reservation'] = request.POST.get('reservation')
    data['text'] = request.POST.get('text')
    data['rating'] = request.POST.get('rating')
    data['date'] = request.POST.get('date')
    review = Review.objects.create(**data)
    data['id'] = review.id
    return JsonResponse(data)

# get all reviews


def review_list(request):
    reviews = Review.objects.all()
    data = {'results': [{'id': review.id, 'listing': review.listing.id, 'guest': review.guest.id,
                         'review': review.review, 'rating': review.rating} for review in reviews]}
    return JsonResponse(data)

# get a single review


def review_detail(request, pk):
    review = get_object_or_404(Review, pk=pk)
    data = {'id': review.id, 'listing': review.listing.id,
            'guest': review.guest.id, }

    return JsonResponse(data)

# update a review


class ReviewUpdate(LoginRequiredMixin, UpdateView):
    model = Review
    fields = ['reservation', 'text', 'rating', 'date']

    def get_object(self, queryset=None):
        review_id = self.kwargs.get('pk')
        return Review.objects.get(id=review_id)

# delete a review


class ReviewDelete(LoginRequiredMixin, DeleteView):
    model = Review

    def get_object(self, queryset=None):
        review_id = self.kwargs.get('pk')
        return Review.objects.get(id=review_id)

    def delete_review(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return JsonResponse({"message": "Review deleted successfully"})


# create an Amenity

def create_amenity(request):
    data = {}
    data['name'] = request.POST.get('name')
    amenity = Amenity.objects.create(**data)
    data['id'] = amenity.id
    return JsonResponse(data)

# get all amenities


def amenity_list(request):
    amenities = Amenity.objects.all()
    data = {'results': [{'id': amenity.id, 'name': amenity.name}
                        for amenity in amenities]}
    return JsonResponse(data)

# get a single amenity


def amenity_detail(request, pk):
    amenity = get_object_or_404(Amenity, pk=pk)
    data = {'id': amenity.id, 'name': amenity.name}
    return JsonResponse(data)


# update an amenity


class AmenityUpdate(LoginRequiredMixin, UpdateView):
    model = Amenity
    fields = ['name']

    def get_object(self, queryset=None):
        amenity_id = self.kwargs.get('pk')
        return Amenity.objects.get(id=amenity_id)

# delete an amenity


class AmenityDelete(LoginRequiredMixin, DeleteView):
    model = Amenity

    def get_object(self, queryset=None):
        amenity_id = self.kwargs.get('pk')
        return Amenity.objects.get(id=amenity_id)

    def delete_amenity(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return JsonResponse({"message": "Amenity deleted successfully"})

# create Amenities for a listing


def create_listing_amenity(request):
    data = {}
    data['listing'] = request.POST.get('listing')
    data['amenity'] = request.POST.get('amenity')
    listing_amenity = ListingAmenity.objects.create(**data)
    data['id'] = listing_amenity.id
    return JsonResponse(data)

# get all listing amenities


def listing_amenity_list(request):
    listing_amenities = ListingAmenity.objects.all()
    data = {'results': [{'id': listing_amenity.id, 'listing': listing_amenity.listing.id, 'amenity': listing_amenity.amenity.id}
                        for listing_amenity in listing_amenities]}
    return JsonResponse(data)

# get a single listing amenity


def listing_amenity_detail(request, pk):
    listing_amenity = get_object_or_404(ListingAmenity, pk=pk)
    data = {'id': listing_amenity.id, 'listing': listing_amenity.listing.id,
            'amenity': listing_amenity.amenity.id}
    return JsonResponse(data)

# update a listing amenity


class ListingAmenityUpdate(LoginRequiredMixin, UpdateView):
    model = ListingAmenity
    fields = ['listing', 'amenity']

    def get_object(self, queryset=None):
        listing_amenity_id = self.kwargs.get('pk')
        return ListingAmenity.objects.get(id=listing_amenity_id)


# delete a listing amenity


class ListingAmenityDelete(LoginRequiredMixin, DeleteView):
    model = ListingAmenity

    def get_object(self, queryset=None):
        listing_amenity_id = self.kwargs.get('pk')
        return ListingAmenity.objects.get(id=listing_amenity_id)

    def delete_listing_amenity(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return JsonResponse({"message": "Listing amenity deleted successfully"})


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
