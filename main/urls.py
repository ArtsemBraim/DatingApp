from django.urls import path
from . import views

urlpatterns = [
    path('profiles/', views.ProfileListView.as_view()),
    path('swipe/', views.SwipeView.as_view())
]
