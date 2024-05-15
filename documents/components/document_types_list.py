from django_unicorn.components import UnicornView
import requests
from dms.settings import SENIOR_DOCTOR_TOKEN


class DocumentTypesListView(UnicornView):
    template_name = "unicorn/document-types-list.html"
    document_types = []
    search = ""
    error = ""

    def mount(self):
        self.load_document_types()

    def load_document_types(self):
        url = "https://intellisoft-dms.fly.dev/documents/document-types/list/"
        headers = {
            "Authorization": SENIOR_DOCTOR_TOKEN
        }

        try:
            response = requests.get(url, headers=headers)

            response.raise_for_status()  # This will raise an exception for HTTP errors
            self.document_types = response.json()
        except requests.RequestException as e:
            self.error = str(e)

    def updated_search(self, search):

        url = "https://intellisoft-dms.fly.dev/documents/document-types/list/?search="
        headers = {
            "Authorization": SENIOR_DOCTOR_TOKEN
        }

        try:
            response = requests.get(url + self.search, headers=headers)

            response.raise_for_status()  # This will raise an exception for HTTP errors
            self.document_types = response.json()
        except requests.RequestException as e:
            self.error = str(e)


