from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.band_list, name="band-list"),
    path('listings/', views.listings, name="listings"),
    path('about-us/', views.about, name="about-us"),
    path('band/<int:id>/', views.band_detail, name="band-detail"),
    path('listing/<int:id>/', views.listing_detail, name="listing-detail"),
    path('listings_band/<int:id>/', views.listings_band, name="listings-band")
]