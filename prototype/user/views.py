from django.contrib.auth import get_user_model
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import UserSerializer, UserSerializerWithToken

User = get_user_model()


class UserViewSet(
    viewsets.GenericViewSet, ListModelMixin, RetrieveModelMixin, CreateModelMixin
):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = UserSerializerWithToken(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    @action(detail=False, methods=["GET"])
    def current_user(self, request):
        """
        Determine the current user by their token, and return their data
        """
        serializer = self.get_serializer(request.user)

        return Response(serializer.data)
