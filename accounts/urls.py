from django.urls import path, include
from accounts.views import RegisterView

urlpatterns = [
    path('acounts/', RegisterView.as_view(), name='register'),
]