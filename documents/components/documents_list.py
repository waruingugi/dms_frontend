from django_unicorn.components import UnicornView
import requests
from dms.settings import SENIOR_DOCTOR_TOKEN


class DocumentsListView(UnicornView):
    template_name = "unicorn/documents-list.html"
    documents = []
    search = ""
    error = ""

    def mount(self):
        self.load_documents()

    def load_documents(self):
        url = "https://intellisoft-dms.fly.dev/documents/list/"
        headers = {
            "Authorization": SENIOR_DOCTOR_TOKEN
        }

        try:
            response = requests.get(url, headers=headers)

            response.raise_for_status()  # This will raise an exception for HTTP errors
            self.documents = response.json()
        except requests.RequestException as e:
            self.error = str(e)

    def updated_search(self, search):

        url = "https://intellisoft-dms.fly.dev/documents/list/?search="
        headers = {
            "Authorization": SENIOR_DOCTOR_TOKEN
        }

        try:
            response = requests.get(url + self.search, headers=headers)

            response.raise_for_status()  # This will raise an exception for HTTP errors
            self.documents = response.json()
        except requests.RequestException as e:
            self.error = str(e)


