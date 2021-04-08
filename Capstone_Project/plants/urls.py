from django.urls import path
from . import views

app_name = 'plants'
urlpatterns = [
    path('', views.index, name='index'),
    path('aboutPage/', views.aboutPage, name='aboutPage'),
    path('food_data/', views.food_data, name='food_data'),
    path('viewFood/', views.viewFood, name="viewFood"),
    path('edamam/', views.edamam, name="edamam")
]