from django.contrib.auth.hashers import make_password
from bnbApp.models import User, Listing, Reservation, Review, Amenity, ListingAmenity
from faker import Faker

fake = Faker()


print('seeding the database....')

# Create 10 users
for i in range(10):
    user = User.objects.create(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        email=fake.email(),
        password=make_password(fake.password()),
        is_host=fake.boolean(chance_of_getting_true=50)
    )


# Create 30 listings of apartments and houses
for i in range(30):
    listing = Listing.objects.create(
        owner=User.objects.get(id=fake.random_int(1, 10)),
        title=fake.sentence(nb_words=3, variable_nb_words=True),
        description=fake.paragraph(nb_sentences=10),
        location=fake.address(),
        price_per_night=fake.random_int(50, 500),
        number_of_rooms=fake.random_int(1, 5),
        max_guests=fake.random_int(1, 10),
        image=fake.image_url()
    )


# Create 50 reservations
for i in range(50):
    reservation = Reservation.objects.create(
        listing=Listing.objects.get(id=fake.random_int(1, 30)),
        guest=User.objects.get(id=fake.random_int(1, 10)),
        start_date=fake.date_between(start_date='-1y', end_date='today'),
        end_date=fake.date_between(start_date='today', end_date='+1y'),
        number_of_guests=fake.random_int(1, 10),
        total_price=fake.random_int(50, 500)
    )


# Create 50 reviews
for i in range(50):
    review = Review.objects.create(
        reservation=Reservation.objects.get(id=fake.random_int(1, 50)),
        text=fake.paragraph(nb_sentences=3),
        rating=fake.random_int(1, 5),
        date=fake.date_between(start_date='-1y', end_date='today')
    )

# Create 10 amenities
amenities = ['Wifi', 'TV', 'Air conditioning', 'Heating', 'Kitchen', 'Washer', 'Dryer', 'Free parking on premises', 'Free street parking', 'Paid parking off premises', 'Elevator', 'Hot tub', 'Pool', 'Gym', 'Breakfast', 'Indoor fireplace', 'Hangers', 'Iron', 'Hair dryer', 'Laptop friendly workspace', 'Private entrance', 'Buzzer/wireless intercom', 'Carbon monoxide detector', 'Smoke detector', 'First aid kit', 'Safety card', 'Fire extinguisher', 'Essentials', 'Shampoo', 'Hangers', 'Hair dryer', 'Laptop friendly workspace', 'Iron', 'Hot water', 'Bed linens', 'Extra pillows and blankets', 'Microwave', 'Refrigerator', 'Dishwasher', 'Cooking basics', 'Oven', 'Stove', 'Coffee maker', 'Dishes and silverware', 'Cooking basics', 'Patio or balcony', 'Garden or backyard', 'Beach essentials', 'Beachfront', 'Waterfront', 'Lake access', 'BBQ grill', 'Fire pit',
             'Bathtub', 'Shower gel', 'Body soap', 'Toilet paper', 'Private living room', 'Beach view', 'Lake view', 'Mountain view', 'Garden or backyard view', 'Pool view', 'Ocean view', 'River view', 'Dining table', 'Coffee maker', 'Dishes and silverware', 'Cooking basics', 'Patio or balcony', 'Garden or backyard', 'Beach essentials', 'Beachfront', 'Waterfront', 'Lake access', 'BBQ grill', 'Fire pit', 'Bathtub', 'Shower gel', 'Body soap', 'Toilet paper', 'Private living room', 'Beach view', 'Lake view', 'Mountain view', 'Garden or backyard view', 'Pool view', 'Ocean view', 'River view', 'Dining table', 'Coffee maker', 'Dishes and silverware', 'Cooking basics', 'Patio or balcony', 'Garden or backyard', 'Beach essentials', 'Beachfront', 'Waterfront', 'Lake access', 'BBQ grill', 'Fire pit', 'Bathtub', 'Shower gel', 'Body soap', 'Toilet paper', 'Private living room',]

for amenity in amenities:
    amenity = Amenity.objects.create(
        name=amenity
    )

# create a list of amenities
amenity_list = Amenity.objects.all()

# create 30 listing amenities
for i in range(30):
    listing = Listing.objects.get(id=fake.random_int(1, 30))
    for amenity in amenity_list:
        listing_amenity = ListingAmenity.objects.create(
            listing=listing,
            amenity=amenity
        )

print('database seeded')
