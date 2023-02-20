from django.db import models

# Create your models here.

# User model


class User(models.Model):
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    email = models.EmailField(unique=True, null=True)
    password = models.CharField(max_length=30, null=True)
    is_host = models.BooleanField(default=False, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

# Listing model


class Listing(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='listings')
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    price_per_night = models.DecimalField(max_digits=7, decimal_places=2)
    number_of_rooms = models.PositiveSmallIntegerField()
    max_guests = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.title

# Reservation model


class Reservation(models.Model):
    listing = models.ForeignKey(
        Listing, on_delete=models.CASCADE, related_name='reservations')
    guest = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reservations')
    start_date = models.DateField()
    end_date = models.DateField()
    number_of_guests = models.PositiveSmallIntegerField()
    total_price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f'{self.guest} - {self.listing} {self.start_date} - {self.end_date}'

# Review model


class Review(models.Model):
    reservation = models.OneToOneField(
        Reservation, on_delete=models.CASCADE, related_name='review')
    text = models.TextField()
    rating = models.PositiveSmallIntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.reservation} - {self.rating} stars'


class Amenity(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

# Many to many relationship between Listing and Amenity


class ListingAmenity(models.Model):
    listing = models.ForeignKey(
        Listing, on_delete=models.CASCADE, related_name='amenities')
    amenity = models.ForeignKey(Amenity, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.listing} - {self.amenity}'

# Many to many relationship between Listing and Location


# class Location(models.Model):
#     name = models.CharField(max_length=100)
#     # reference to the name of a listing and set it to null if the listing is deleted
#     listings = models.ManyToManyField(Listing, related_name='locations')

#     def __str__(self):
#         return self.name
