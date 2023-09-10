from django.urls import path
from recipe1 import views
urlpatterns = [
    path('recipepage1',views.recipe1)
]