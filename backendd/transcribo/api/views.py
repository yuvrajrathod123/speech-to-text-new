


from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .models import Reservation, Equipment, Refreshment, UserRegistration, Participant
from .serializers import ReservationSerializer, EquipmentSerializer, RefreshmentSerializer,  ParticipantSerializer, UserRegistrationSerializer
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password 




class ReservationListView(ListAPIView):
    # queryset = Reservation.objects.all()
    # serializer_class = ReservationSerializer
    
    def get(self, request):
        reservations = Reservation.objects.all()
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data)

class ReservationCreateView(CreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer



class ReservationRetrieveView(RetrieveAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class ReservationUpdateView(UpdateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class ReservationDeleteView(DestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class EquipmentListView(ListAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

class RefreshmentListView(ListAPIView):
    queryset = Refreshment.objects.all()
    serializer_class = RefreshmentSerializer



# taking input of participants email and all
class ParticipantCreateView(CreateAPIView):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data, many=True)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response({'message': 'Participants added successfully!', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(f'Error: {str(e)}')
            return Response({'error': 'An error occurred while processing the request.'}, status=status.HTTP_400_BAD_REQUEST)


class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save user registration data to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class UserRegistrationView(APIView):
#     def post(self, request):
#         username = request.data.get('username')
#         email = request.data.get('email')
#         password = request.data.get('password')

#         # Hash the password using make_password
#         hashed_password = make_password(password)

#         # Create a new user with the hashed password
#         user = UserRegistration(username=username, email=email, password=hashed_password)
#         user.save()

#         # You can also authenticate and login the user here if needed

#         return Response({'message': 'User registration successful'}, status=201)
    

# # views.py
# from django.http import JsonResponse
# from rest_framework.views import APIView
# from rest_framework.response import Response

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = UserRegistration.objects.get(username=username, password=password)
        print(f"Received username: {username}")
        print(f"Received password: {password}")
        print(f"{user}")

        if user is not None:
            login(request, user)
            if user.username == 'admin' and user.password == '@Admin':
                return Response({'message': 'Admin login successful', 'isAdmin': True}, status=200)
            else:
                return Response({'message': 'User login successful', 'isAdmin': False}, status=200)
        else:
            return Response({'error': 'Invalid username or password'}, status=400)
