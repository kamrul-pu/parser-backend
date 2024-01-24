"""Views for candidate profiles."""
from rest_framework.permissions import (
    IsAuthenticated,
)
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)


from candidate.rest.serializers.profiles import (
    ProfileListSerializer,
    ProfileDetailSerializer,
)

from candidate.models import Profile


class ProfileList(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileListSerializer
    queryset = Profile.objects.filter().order_by("-created_at")


class ProfileDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileDetailSerializer
    queryset = Profile.objects.filter()