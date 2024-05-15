from django.views.generic import TemplateView


class UsersView(TemplateView):
    template_name = "users.html"


class AddUsersView(TemplateView):
    template_name = "add_users.html"

