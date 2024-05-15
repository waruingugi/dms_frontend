from django.views.generic import TemplateView


class DocumentsView(TemplateView):
    template_name = "documents.html"


class DocumentTypesView(TemplateView):
    template_name = "document_types.html"


class DocumentVersionsView(TemplateView):
    template_name = "document_versions.html"
