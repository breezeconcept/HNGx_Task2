from rest_framework import generics
from .models import Person
from .serializers import PersonSerializer

class PersonListCreateView(generics.ListCreateAPIView):
    serializer_class = PersonSerializer

    def get_queryset(self):
        queryset = Person.objects.all()
        name = self.request.query_params.get('name')
        
        if name:
            queryset = queryset.filter(name=name)
        
        return queryset

    def perform_create(self, serializer):
        serializer.save()

class PersonDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
