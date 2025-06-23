from django.urls import path
from users.views import *

urlpatterns = [
    # User endpoints
    path(
        "users/<slug:username>/", 
        UserProfileView.as_view(), 
        name="user-profile"
    ),

    path(
        "update-profile/", 
        UpdateProfileView.as_view(), 
        name="update-profile"
    ),
]