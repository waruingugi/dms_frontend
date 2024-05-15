from django_unicorn.components import UnicornView
import requests
from dms.settings import SENIOR_DOCTOR_TOKEN


class CreateUserView(UnicornView):
    template_name = "unicorn/create-user.html"

    error = ""
    role = ""
    first_name = ""
    last_name = ""
    email = ""

    def create(self):
        try:
            payload = {
                "email": self.email,
                "first_name": self.first_name,
                "last_name": self.last_name,
                "role": self.role
            }


            # URL of the API endpoint
            url = "https://intellisoft-dms.fly.dev/auth/user/create/"

            # Sending the payload as JSON
            headers = {
                'Content-Type': 'application/json',
                "Authorization": SENIOR_DOCTOR_TOKEN
            }

            # Make a POST request
            response = requests.post(url, json=payload, headers=headers)
            print(response.json())

        except requests.RequestException as e:
            self.error = str(e)