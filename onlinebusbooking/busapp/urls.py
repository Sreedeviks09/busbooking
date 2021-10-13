from . import views
from django.urls import path

urlpatterns = [
    path('', views.busbooking, name='busbooking'),
    path('booking/',views.booking,name='booking'),
    path('response/', views.response, name='response'),
]
