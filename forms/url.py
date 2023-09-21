from django.urls import path
from .views import ContactFormList

urlpatterns = [
    path('forms/', ContactFormList.as_view()),
]
