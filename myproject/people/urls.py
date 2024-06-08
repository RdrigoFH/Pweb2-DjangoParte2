# people/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Function-based view
    path('person/<int:id>/', views.PersonDetailView.as_view(), name='person_detail'),  # Class-based view
]
