from django.urls import path, include
from .views import Memo

urlpatterns = [
    path('memo/', Memo),
]
