from django.urls import path


from candidate.rest.views.profiles import ProfileList, ProfileDetail

urlpatterns = [
    path("", ProfileList.as_view(), name="profile-list-create"),
    path("/<int:pk>", ProfileDetail.as_view(), name="profile-detail"),
]