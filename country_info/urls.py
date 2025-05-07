from django.urls import path
from views import CountryViewSet

urlpatterns = [
    path('countries/', CountryViewSet.as_view({'get':'list'}), name='country-list'),
]
