from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('authors', views.show),
    path('books', views.books),
    path('new', views.authors),
    path('books/<int:id>', views.book_des,name = 'id_detail'),
    path('authadd', views.author_add),
    path('authors/<int:id>', views.auth_des,name = 'author_detail' ),
    path('bookadd',views.book_add),
]