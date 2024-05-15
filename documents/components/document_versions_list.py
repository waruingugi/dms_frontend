from django_unicorn.components import UnicornView
import requests
from dms.settings import SENIOR_DOCTOR_TOKEN


class DocumentVersionsListView(UnicornView):
    template_name = "unicorn/document-versions-list.html"
    document_versions = []
    search = ""
    error = ""

    def mount(self):
        self.load_document_versions()

    def load_document_versions(self):
        url = "https://intellisoft-dms.fly.dev/documents/history/"
        headers = {
            "Authorization": SENIOR_DOCTOR_TOKEN
        }

        try:
            response = requests.get(url, headers=headers)

            response.raise_for_status()  # This will raise an exception for HTTP errors
            self.document_versions = response.json()

        except requests.RequestException as e:
            self.error = str(e)

    def updated_search(self, search):

        url = "https://intellisoft-dms.fly.dev/documents/history/?search="
        headers = {
            "Authorization": SENIOR_DOCTOR_TOKEN
        }

        try:
            response = requests.get(url + self.search, headers=headers)

            response.raise_for_status()  # This will raise an exception for HTTP errors
            self.document_versions = response.json()
        except requests.RequestException as e:
            self.error = str(e)


