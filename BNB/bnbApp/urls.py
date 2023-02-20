from django.urls import path
from .views import *  # import all views from views.py

urlpatterns = [
    # home page
    # path('', home_view, name='home'),
    # user urls
    path('user/create/', user_create, name='user_create'),
    path('user/list/', user_list, name='user_list'),
    path('user/<int:pk>/', user_detail, name='user_detail'),
    path('user/<int:pk>/update/', user_update, name='user_update'),
    path('user/<int:pk>/delete/', user_delete, name='user_delete'),

    # listing urls
    path('listing/create/', listing_create, name='listing_create'),
    path('listing/list/', listing_list, name='listing_list'),
    path('listing/<int:pk>/', listing_detail, name='listing_detail'),
    path('listing/<int:pk>/update/',
         listing_update, name='listing_update'),
    path('listing/<int:pk>/delete/',
         listing_delete, name='listing_delete'),

    # reservation urls
    path('reservation/create/', create_reservation, name='reservation_create'),
    path('reservation/list/', reservation_list, name='reservation_list'),
    path('reservation/<int:pk>/', reservation_detail, name='reservation_detail'),
    path('reservation/<int:pk>/update/',
         ReservationUpdate.as_view(), name='reservation_update'),
    path('reservation/<int:pk>/delete/',
         ReservationDelete.as_view(), name='reservation_delete'),

    # reviews urls
    path('review/create/', create_review, name='review_create'),
    path('review/list/', review_list, name='review_list'),
    path('review/<int:pk>/', review_detail, name='review_detail'),
    path('review/<int:pk>/update/', ReviewUpdate.as_view(), name='review_update'),
    path('review/<int:pk>/delete/', ReviewDelete.as_view(), name='review_delete'),

    # amenity urls
    path('amenity/create/', create_amenity, name='amenity_create'),
    path('amenity/list/', amenity_list, name='amenity_list'),
    path('amenity/<int:pk>/', amenity_detail, name='amenity_detail'),
    path('amenity/<int:pk>/update/',
         AmenityUpdate.as_view(), name='amenity_update'),
    path('amenity/<int:pk>/delete/',
         AmenityDelete.as_view(), name='amenity_delete'),

    # listing amenity urls
    path('listing_amenity/create/', create_listing_amenity,
         name='listing_amenity_create'),
    path('listing_amenity/list/', listing_amenity_list,
         name='listing_amenity_list'),
    path('listing_amenity/<int:pk>/', listing_amenity_detail,
         name='listing_amenity_detail'),
    path('listing_amenity/<int:pk>/update/',
         ListingAmenityUpdate.as_view(), name='listing_amenity_update'),
    path('listing_amenity/<int:pk>/delete/',
         ListingAmenityDelete.as_view(), name='listing_amenity_delete'),

    # location urls
    #     path('location/create/', create_location, name='location_create'),
    #     path('location/list/', location_list, name='location_list'),
    #     path('location/<int:pk>/', location_detail, name='location_detail'),
    #     path('location/<int:pk>/update/',
    #          LocationUpdate.as_view(), name='location_update'),
    #     path('location/<int:pk>/delete/',
    #          LocationDelete.as_view(), name='location_delete'),

]  # end of urlpatterns
