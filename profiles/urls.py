from django.urls import path
from . import views


urlpatterns = [
    path('detail/', views.ProfileDetailView.as_view())
]