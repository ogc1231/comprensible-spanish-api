from django.urls import path
from favourites import views

urlpatterns = [
    path('favourites/', views.FollowerList.as_view()),
    path('favourites/<int:pk>/', views.FollowerDetail.as_view())
]