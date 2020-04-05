from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.render_books_home),
    path('add_book', views.add_book),
    path('<int:id>', views.render_book_page),
    path('update_book/<int:id>', views.update_book),
    path('delete_book/<int:id>', views.delete_book),
    path('add_favorite/<int:id>', views.add_favorite)
]