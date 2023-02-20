from django.contrib.auth.hashers import make_password
from bnbApp.models import User, Listing, Reservation, Review
from faker import Faker

fake = Faker()

# Create 10 users
for i in range(10):
    user = User.objects.create(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        email=fake.email(),
        password=make_password(fake.password()),
        is_host=fake.boolean(chance_of_getting_true=50)
    )


# Create 30 listings
for i in range(30):
    listing = Listing.objects.create(
        owner=User.objects.get(id=fake.random_int(1, 10)),
        title=fake.sentence(nb_words=3),
        description=fake.paragraph(nb_sentences=3),
        location=fake.city(),
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
