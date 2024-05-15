from django_unicorn.components import UnicornView
import requests
from dms.settings import SENIOR_DOCTOR_TOKEN


class UsersListView(UnicornView):
    template_name = "unicorn/users-list.html"
    users = []
    search = ""
    error = ""

    def mount(self):
        self.load_users()

    def load_users(self):
        url = "https://intellisoft-dms.fly.dev/auth/user/list/"
        headers = {
            "Authorization": SENIOR_DOCTOR_TOKEN
        }

        try:
            response = requests.get(url, headers=headers)

            response.raise_for_status()  # This will raise an exception for HTTP errors
            self.users = response.json()
        except requests.RequestException as e:
            self.error = str(e)

    def updated_search(self, search):

        url = "https://intellisoft-dms.fly.dev/auth/user/list/?search="
        headers = {
            "Authorization": SENIOR_DOCTOR_TOKEN
        }

        try:
            response = requests.get(url + self.search, headers=headers)

            response.raise_for_status()  # This will raise an exception for HTTP errors
            self.users = response.json()
        except requests.RequestException as e:
            self.error = str(e)


