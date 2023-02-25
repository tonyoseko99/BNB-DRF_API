from django.db import models
from django.forms import ValidationError

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
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title

    def clean(self):
        if self.number_of_rooms < 1:
            raise ValidationError(
                f'Number of rooms must be greater than 0')

        if self.max_guests < 1:
            raise ValidationError(
                f'Maximum number of guests must be greater than 0')


# Reservation model


class Reservation(models.Model):
    listing = models.ForeignKey(
        Listing, on_delete=models.CASCADE, related_name='reservations')
    guest = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reservations')
    start_date = models.DateField(auto_now_add=True)  # auto_now_add=True
    end_date = models.DateField()
    number_of_guests = models.PositiveSmallIntegerField()
    total_price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f'{self.guest} - {self.listing} {self.start_date} - {self.end_date}'

    def clean(self):
        reservations = self.listing.reservations.all()
        for reservation in reservations:
            if self.start_date <= reservation.end_date and self.end_date >= reservation.start_date:
                raise ValidationError(
                    f'Listing is already reserved for this date range')

        if self.start_date > self.end_date:
            raise ValidationError(
                f'Start date must be before end date')

        if self.number_of_guests > self.listing.max_guests:
            raise ValidationError(
                f'Number of guests must be less than or equal to {self.listing.max_guests}')

        if self.number_of_guests < 1:
            raise ValidationError(
                f'Number of guests must be greater than 0')

        if self.start_date < self.listing.reservations.all().order_by('-end_date').first().end_date:
            raise ValidationError(
                f'Start date must be after {self.listing.reservations.all().order_by("-end_date").first().end_date}')

        if (self.end_date - self.start_date).days > 30:
            raise ValidationError(
                f'Reservation cannot be longer than 30 days')


# Review model


class Review(models.Model):
    reservation = models.ForeignKey(
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
