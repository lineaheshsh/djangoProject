from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('board/', views.board),
    path('board/new_board', views.new_board),
    path('board/<int:pk>/', views.edit_board),
    path('board/<int:pk>/remove/', views.del_board)
]