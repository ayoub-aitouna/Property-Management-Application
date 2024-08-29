from django.shortcuts import render
from rest_framework import generics, status
from users.serializers import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.db import IntegrityError


class RegisterUser(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            get_user_model().objects.create_user(**serializer.validated_data)
        except IntegrityError as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'detail': 'User with this username already exists'})
        except Exception as e:
            print(f'error => {e}')
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'detail': str(e)})
        return Response(status=status.HTTP_201_CREATED)
