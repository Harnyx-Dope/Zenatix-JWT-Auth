
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Event, Registration, Venue, Category,User
from .serializers import UserSerializer, EventSerializer, RegistrationSerializer, VenueSerializer, CategorySerializer

 

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    authentication_classes=[JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # if user.is_authenticated and user.username == self.request.user:
        #     return Event.objects.all()
        # else:
        return Event.objects.all()

    

class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
     
     

    # def perform_create(self, serializer):
    #     user = self.request.user
    #     if isinstance(user, User):
    #         serializer.save(user=self.request.user)



class VenueViewSet(viewsets.ModelViewSet):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
