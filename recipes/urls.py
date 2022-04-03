from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeListView.as_view(), name = 'homepage'),
    path('form/', views.index, name = 'index'),
    path('<int:recipe_id>/', views.detail, name = 'detail'),
    path('success/', views.result ,name = 'success'),
    path('short/', views.short, name = 'short'),
    path('long/', views.long, name = 'long'),
    path('<int:recipe_id>/fork/', views.fork, name = 'fork'),
    path('<int:recipe_id>/add/', views.add, name = 'add'),
    path('myrecipes/', views.myrecipes, name = 'myrecipes'),
    path('favorited_list/', views.favorited_list, name='favorited_list'),
    path('favorite/', views.favorite_recipe, name='favorite_recipe')
]