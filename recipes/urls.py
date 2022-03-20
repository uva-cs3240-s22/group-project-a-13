from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeListView.as_view(), name = 'homepage'),
    path('form/', views.index, name = 'index'),
    path('<int:recipe_id>/', views.detail, name = 'detail'),
    path('success/', views.result ,name = 'success'),
]