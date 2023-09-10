from django.urls import path
from Signup import views
urlpatterns = [
    path('signup',views.signup)
]