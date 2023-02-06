from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from django.views.generic import UpdateView, DeleteView


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

# update a user


class UserUpdate(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email', 'password', 'is_host']

    def get_object(self, queryset=None):
        user_id = self.kwargs.get('pk')
        return User.objects.get(id=user_id)

# delete a user


class UserDelete(LoginRequiredMixin, DeleteView):
    model = User

    def get_object(self):
        return self.request.user


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

# update a listing


class ListingUpdate(LoginRequiredMixin, UpdateView):
    model = Listing
    fields = ['title', 'description', 'location',
              'price_per_night', 'number_of_rooms', 'max_guests']

    def get_object(self, queryset=None):
        listing_id = self.kwargs.get('pk')
        return Listing.objects.get(id=listing_id)

# get all reservations


def reservation_list(request):
    reservations = Reservation.objects.all()
    data = {'results': [{'id': reservation.id, 'listing': reservation.listing.id, 'guest': reservation.guest.id, 'start_date': reservation.start_date, 'end_date': reservation.end_date,
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
