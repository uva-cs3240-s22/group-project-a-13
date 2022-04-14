from django.urls import path
from . import views
from .views import SearchResultsView

urlpatterns = [
    path('', views.homeListView.as_view(), name = 'homepage'),
    path('form/', views.index, name = 'index'),
    path('<int:recipe_id>/', views.detail, name = 'detail'),
    path('success/', views.result ,name = 'success'),
    path('short/', views.short, name = 'short'),
    path('search/', views.SearchResultsView.as_view(), name = 'search'),
    path('login/', views.login, name = 'login'),
    path('long/', views.long, name = 'long'),
    path('<int:recipe_id>/fork/', views.fork, name = 'fork'),
    path('<int:recipe_id>/add/', views.add, name = 'add'),
    path('<int:recipe_id>/add_e/', views.add_e, name = 'add_e'),
    path('<int:recipe_id>/add_i/', views.add_i, name = 'add_i'),
    path('<int:recipe_id>/add_instruction/', views.add_instruction, name = 'add_instruction'),
    path('<int:recipe_id>/add_equipment/', views.add_equipment, name = 'add_equipment'),
    path('<int:recipe_id>/add_ingredient/', views.add_ingredient, name = 'add_ingredient'),
    path('<int:recipe_id>/edit_description/', views.edit_description, name = 'edit_description'),
    path('<int:recipe_id>/edit_d/', views.edit_d, name = 'edit_d'),
    path('myrecipes/', views.myrecipes, name = 'myrecipes'),
    path('favorited_list/', views.favorited_list, name='favorited_list'),
    path('favorite/', views.favorite_recipe, name='favorite_recipe'),
    path('<int:instruction_id>/<int:recipe_id>/delete_instruction/', views.delete_instruction, name = 'delete_instruction'),
    path('<int:equipment_id>/<int:recipe_id>/delete_equipment/', views.delete_equipment, name = 'delete_equipment'),
    path('<int:ingredient_id>/<int:recipe_id>/delete_ingredient/', views.delete_ingredient, name = 'delete_ingredient'),

]