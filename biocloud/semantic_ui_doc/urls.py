from django.conf.urls import url
from .views import GridView, BootstrapView

urlpatterns = [
    url('^grid/$', GridView.as_view(), name='semantic_ui_grid'),
    url('^bootstrap/$', BootstrapView.as_view(), name='semantic_ui_bootstrap'),
]
