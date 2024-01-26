"""Views for open jobs."""

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    IsAdminUser,
)

from recruitment.models import OpenJobs
from recruitment.rest.serializers.open_jobs import (
    OpenJobListSerializer,
    OpenJobDetailSerializer,
)


class OpenJobList(ListCreateAPIView):
    queryset = OpenJobs().get_all_actives()
    permission_classes = (IsAuthenticated,)
    serializer_class = OpenJobListSerializer


class OpenJobDetail(RetrieveUpdateDestroyAPIView):
    queryset = OpenJobs().get_all_actives()
    permission_classes = (IsAdminUser,)
    serializer_class = OpenJobDetailSerializer
