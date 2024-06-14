from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_info_view),
    path('user_info_table/', views.user_info_table, name='user_info_table'),
    path('update_user/<int:pk>/', views.update_user_view, name='update_user'),
    path('delete_user/<int:pk>/', views.delete_user_view, name='delete_user'),
    path('user_info/', views.user_info_view, name='user_info_view'),

]