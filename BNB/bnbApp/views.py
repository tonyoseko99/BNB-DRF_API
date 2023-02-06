from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from django.views.generic import UpdateView, DeleteView

from .serializers import UserSerializer, ListingSerializer, ReservationSerializer, ReviewSerializer, AmenitySerializer, LocationSerializer
from .models import User, Listing, Reservation, Review, Amenity, Location, ListingAmenity


# create a user


def user_create(request):
    if request.method == 'POST':
        user = User.objects.create_user(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            email=request.POST.get('email'),
            password=request.POST.get('password'),
            is_host=request.POST.get('is_host')
        )
        data = {'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name,
                'email': user.email, 'password': user.password, 'is_host': user.is_host}
        return JsonResponse(data)

# get all users


def user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)

    return JsonResponse(serializer.data, safe=False)

# get a single user


def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    serializer = UserSerializer(user)

    return JsonResponse(serializer.data)

# update a user


class UserUpdate(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email', 'password', 'is_host']

    def get_object(self, queryset=None):
        user_id = self.kwargs.get('pk')
        return User.objects.get(id=user_id)

    def form_valid(self, form):
        try:
            user = form.save(commit=False)
            user.save()
            return JsonResponse({'message': 'User updated successfully'})
        except Exception as e:
            return JsonResponse({'message': str(e)})


# delete a user


class UserDelete(LoginRequiredMixin, DeleteView):
    model = User

    def get_object(self, queryset=None):
        user_id = self.kwargs.get('pk')
        return User.objects.get(id=user_id)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return JsonResponse({'message': 'User deleted successfully'})

# create a listing


def listing_create(request):
    listing = Listing.objects.create(
        owner=request.POST.get('owner'),
        title=request.POST.get('title'),
        description=request.POST.get('description'),
        location=request.POST.get('location'),
        price_per_night=request.POST.get('price_per_night'),
        number_of_rooms=request.POST.get('number_of_rooms'),
        max_guests=request.POST.get('max_guests')
    )
    data = {'id': listing.id, 'owner': listing.owner.id, 'title': listing.title, 'description': listing.description, 'location': listing.location.id,
            'price_per_night': listing.price_per_night, 'number_of_rooms': listing.number_of_rooms, 'max_guests': listing.max_guests}
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

# update a listing


class ListingUpdate(LoginRequiredMixin, UpdateView):
    model = Listing
    fields = ['title', 'description', 'location',
              'price_per_night', 'number_of_rooms', 'max_guests']

    def get_object(self, queryset=None):
        listing_id = self.kwargs.get('pk')
        return Listing.objects.get(id=listing_id)

    # update listing

    def form_valid(self, form):
        try:
            listing = form.save(commit=False)
            listing.save()
            return JsonResponse({'message': 'Listing updated successfully'})
        except Exception as e:
            return JsonResponse({'message': str(e)})

# delete a listing


class ListingDelete(LoginRequiredMixin, DeleteView):
    model = Listing
    #  get the listing object by id

    def get_object(self, queryset=None):
        listing_id = self.kwargs.get('pk')
        return Listing.objects.get(id=listing_id)

    # delete listing
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return JsonResponse({"message": "Listing deleted Successfully"})

# create a reservation


def create_reservation(request):
    data = {}
    data['listing'] = request.POST.get('listing')
    data['guest'] = request.POST.get('guest')
    data['start_date'] = request.POST.get('start_date')
    data['end_date'] = request.POST.get('end_date')
    data['number_of_guests'] = request.POST.get('number_of_guests')
    data['total_price'] = request.POST.get('total_price')
    reservation = Reservation.objects.create(**data)
    data['id'] = reservation.id
    return JsonResponse(data)

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


# create a location


def create_location(request):
    data = {}
    data['name'] = request.POST.get('name')
    data['listings'] = request.POST.get('listings')
    location = Location.objects.create(**data)
    data['id'] = location.id
    return JsonResponse(data)

# get all locations


def location_list(request):
    locations = Location.objects.all()
    data = {'results': [{'id': location.id, 'name': location.name, 'listings': location.listings}
                        for location in locations]}
    return JsonResponse(data)

# get a single location


def location_detail(request, pk):
    location = get_object_or_404(Location, pk=pk)
    data = {'id': location.id, 'name': location.name,
            'listings': location.listings}
    return JsonResponse(data)

# update a location


class LocationUpdate(LoginRequiredMixin, UpdateView):
    model = Location
    fields = ['name', 'listings']

    def get_object(self, queryset=None):
        location_id = self.kwargs.get('pk')
        return Location.objects.get(id=location_id)

# delete a location


class LocationDelete(LoginRequiredMixin, DeleteView):
    model = Location

    def get_object(self, queryset=None):
        location_id = self.kwargs.get('pk')
        return Location.objects.get(id=location_id)

    def delete_location(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return JsonResponse({"message": "Location deleted successfully"})
