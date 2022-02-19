from django.urls import path
from CATAPP import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('search/result', views.search, name='search'),
]