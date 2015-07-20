from django.views.generic.base import TemplateView

class GridView(TemplateView):

    template_name = 'semantic_ui_doc/grid.html'

class BootstrapView(TemplateView):

    template_name = 'semantic_ui_doc/bootstrap.html'
