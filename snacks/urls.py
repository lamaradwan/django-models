from django.contrib import admin
from django.urls import path, include
from snacks.views import SnackListView, SnackDetailView

urlpatterns = [
    path('', SnackListView.as_view(), name='snacks'),
    path('<int:pk>/', SnackDetailView.as_view(), name='snack_detail')
]

