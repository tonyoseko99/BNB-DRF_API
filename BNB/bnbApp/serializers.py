from rest_framework import serializers
from .models import User, Listing, Reservation, Review, Amenity, ListingAmenity


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name',
                  'email', 'password', 'is_host', ]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'


class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = ['name']


class ListingAmenitySerializer(serializers.ModelSerializer):
    amenity = AmenitySerializer(read_only=True)

    class Meta:
        model = ListingAmenity
        # fields should show the name property of the amenity
        fields = ['amenity']


class ListingSerializer(serializers.ModelSerializer):
    amenities = ListingAmenitySerializer(read_only=True, many=True)
    reservations = ReservationSerializer(read_only=True, many=True)
    review = ReviewSerializer(read_only=True, many=True)

    class Meta:
        model = Listing
        fields = ['id', 'title', 'description', 'location',
                  'price_per_night', 'number_of_rooms', 'max_guests', 'image', 'amenities', 'reservations', 'review']


# class LocationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Location
#         fields = '__all__'
