from django.urls import path
from .views import index

urlpatterns = [
    path('<int:pk>/', index), # /1 /2 /101241
]

