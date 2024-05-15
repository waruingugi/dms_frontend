from django.urls import path

from documents.views import DocumentsView, DocumentTypesView, DocumentVersionsView

app_name = "documents"

urlpatterns = [
    # Component urls
    path("", DocumentsView.as_view(), name="documents"),
    path("document-types", DocumentTypesView.as_view(), name="document-types"),
    path("document-versions", DocumentVersionsView.as_view(), name="document-versions"),
]
