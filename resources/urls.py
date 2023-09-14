from django.urls import path
from resources import views

urlpatterns = [
    path('resources/', views.ResourceList.as_view()),
    path('resources/<int:pk>/', views.ResourceDetail.as_view())
]