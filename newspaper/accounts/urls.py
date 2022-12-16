from django.urls import path
from accounts import views
from .views import *

urlpatterns = [
    path('signup/', SingUpView.as_view(), name='signup'),
]
