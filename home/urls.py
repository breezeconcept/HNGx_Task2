from django.urls import path
from .views import PersonListCreateView, PersonDetailView

urlpatterns = [
    path('api/', PersonListCreateView.as_view(), name='person-list-create'),
    path('api/<int:pk>/', PersonDetailView.as_view(), name='person-detail'),
]
