"""Views for Match model."""

from rest_framework import status
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    IsAdminUser,
)
from rest_framework.response import Response


from recruitment.models import Match, OpenJobs
from recruitment.rest.serializers.match import (
    MatchListSerializer,
    MatchDetailSerializer,
)
from recruitment.utils import generate_job_matched_profile


class MatchList(ListCreateAPIView):
    queryset = Match().get_all_actives()
    serializer_class = MatchListSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        # Retrieve job_id from request data
        job_id: int = request.data.get("job_id", None)
        if job_id:
            # Retrieve the OpenJobs object with the provided job_id
            job: OpenJobs = OpenJobs().get_all_actives().filter(id=job_id).first()
            # Check if the job is valid
            if job is None:
                # Return error response if the job is not valid
                return Response(
                    {"detail": "Invalid open job id. Please provide a valid id."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            # Generate matched profiles for the provided job_id
            matches = generate_job_matched_profile(job_id=job.id)
            # Serialize the generated matches
            result = self.serializer_class(matches)
            # Return success response with the generated matches
            return Response(
                {"detail": "Match generated successfully", "result": result.data},
                status=status.HTTP_200_OK,
            )
        # Return error response if job_id is not provided
        return Response(
            {"detail": "You need to provide a job id to generate match."},
            status=status.HTTP_400_BAD_REQUEST,
        )


class MatchDetail(RetrieveUpdateDestroyAPIView):
    queryset = Match().get_all_actives()
    serializer_class = MatchDetailSerializer
    permission_classes = (IsAuthenticated,)
