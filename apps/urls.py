from django.urls import path
from apps.views import HomeView

app_name = "apps"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
]