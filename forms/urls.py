from django.urls import path
from forms import views

urlpatterns = [
    path('forms/', views.ContactFormList.as_view()),
]
