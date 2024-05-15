from django.urls import path

from users.views import UsersView, AddUsersView

app_name = "users"

urlpatterns = [
    # Component urls
    path("", UsersView.as_view(), name="users"),
    path("create", AddUsersView.as_view(), name="create-user"),
]
