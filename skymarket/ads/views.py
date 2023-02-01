from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from ads.models import *
from ads.permissions import IsAdOwnerOrStaff
from ads.serializers import *
from ads.filters import *


class AdPagination(pagination.PageNumberPagination):
    pass


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdFilter

    default_permissions = [AllowAny()]
    permissions = {
        'retrieve': [IsAuthenticated()],
        'update': [IsAuthenticated(), IsAdOwnerOrStaff()],
        'create': [IsAuthenticated()],
        'partial_update': [IsAuthenticated(), IsAdOwnerOrStaff()],
        'destroy': [IsAuthenticated(), IsAdOwnerOrStaff()],
    }

    def get_permissions(self):
        return self.permissions.get(self.action, self.default_permissions)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    default_permissions = [AllowAny()]
    permissions = {
        'retrieve': [IsAuthenticated()],
        'update': [IsAuthenticated(), IsAdOwnerOrStaff()],
        'create': [IsAuthenticated()],
        'list': [IsAuthenticated()],
        'partial_update': [IsAuthenticated(), IsAdOwnerOrStaff()],
        'delete': [IsAuthenticated(), IsAdOwnerOrStaff()],
    }

    def get_permissions(self):
        return self.permissions.get(self.action, self.default_permissions)
