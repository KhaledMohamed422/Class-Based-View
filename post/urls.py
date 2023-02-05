from django.urls import path
from . import views

urlpatterns = [
    path('PostList/', views.PostList.as_view(), name='PostList'),
    path('PostDetail/<int:pk>/', views.PostDetail.as_view(), name='PostDetail'),
    # path('contact/', views.contact, name='contact'),
]