from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import permissions, viewsets

from .models import Pet, User
from .permissions import IsOwnerOrReadOnly
from .serializers import PetSerializer, UserSerializer


class PetViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling CRUD operations on the Pet model.
    """

    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ("kind",)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A ViewSet for retrieving user information.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        """
        The queryset for retrieving users
        with prefetching of related pet information.
        """
        queryset = User.objects.all()
        queryset = queryset.prefetch_related("pet_set")

        return queryset
