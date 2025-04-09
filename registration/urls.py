from django.urls import path
from .views import user_info

urlpatterns = [
    # path('', index, name='index'),
    path('registration/', user_info, name=('user_registration'))
]