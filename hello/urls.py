from django.contrib import admin
from django.urls import path

from hello.views import hello_world, hello_china, test_html, not_404, test_redirect

urlpatterns = [
    path('world/<int:month>/', hello_world, name='hello_world'),
    path('china/', hello_china, name='hello_china'),
    path('html/', test_html, name='test_html'),
    path('not_404/', not_404, name="not_404"),
    path('redirect/', test_redirect, name="test_redirect")
]
