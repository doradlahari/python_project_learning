from django.urls import  path
from . import views
urlpatterns = [
    path('sample/', views.sample_page, name='sample_page'),
    path('register/', views.register_page, name='register_page'),
]

