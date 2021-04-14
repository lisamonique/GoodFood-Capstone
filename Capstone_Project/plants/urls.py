from django.urls import path
from . import views

app_name = 'plants'
urlpatterns = [
    path('', views.index, name='index'),
    path('aboutPage/', views.aboutPage, name='aboutPage'),
    path('foodData/', views.foodData, name='foodData'),
    path('viewRecipe/', views.viewRecipe, name="viewRecipe"),
    path('edamam/', views.edamam, name="edamam"),
    path('dashboard/', views.dashboard, name="dashboard")
]