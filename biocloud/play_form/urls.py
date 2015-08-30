from django.conf.urls import url
from .views import example_form, example_multiform

urlpatterns = [
    url(r'^simple$', example_form, name='example_form'),
    url(r'^multi$', example_multiform, name='example_multiform'),
]
