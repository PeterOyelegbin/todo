from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('about/', views.AboutPage.as_view(), name='about'),
    path('create/', views.AddItem.as_view(), name='create'),
    path('<int:pk>/', views.DetailItem.as_view(), name='details'),
    path('edit/<int:pk>/', views.UpdateItem.as_view(), name='update'),
    path('delete/<int:pk>/', views.DeleteItem.as_view(), name='delete'),
]