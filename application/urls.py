from django.urls import path
from .views import login_view, info_view

urlpatterns = [
    path('', login_view, name='login_view'),
    path('', info_view, name='info_view'),
]
