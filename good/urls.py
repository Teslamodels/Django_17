from django.urls import path
from .views import Port, Port2

urlpatterns = [
    path('', Port.as_view(), name='home'),
    path('post/<int:pk>/', Port2.as_view(), name='detail'),
]