from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.hello),
    path('listings/', views.listings),
    path('about-us/', views.about)
]