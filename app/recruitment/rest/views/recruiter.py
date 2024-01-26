"""Views for recruiters."""

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from rest_framework.permissions import IsAuthenticated, IsAdminUser

from recruitment.models import Recruiter

from recruitment.rest.serializers.recruiter import (
    RecruiterListSerializer,
    RecruiterDetailSerializer,
)


class RecruiterList(ListCreateAPIView):
    serializer_class = RecruiterListSerializer
    queryset = Recruiter().get_all_actives()
    permission_classes = (IsAuthenticated,)


class RecruiterDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = RecruiterDetailSerializer
    permission_classes = (IsAdminUser,)
    queryset = Recruiter().get_all_actives()
