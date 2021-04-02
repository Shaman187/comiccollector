from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('comics/', views.comics_index, name='index'),
    path('comics/<int:comic_id>/', views.comics_detail, name='detail'),
    path('comics/<int:comic_id>/add_reading/', views.add_reading, name='add_reading'),
    path('comics/<int:comic_id>/assoc_genre/<int:genre_id>/', views.assoc_genre, name='assoc_genre'),
    path('comics/<int:comic_id>/unassoc_genre/<int:genre_id>/', views.unassoc_genre, name='unassoc_genre'),
    path('comics/<int:comic_id>/add_photo/', views.add_photo, name='add_photo'),
    path('comics/create/', views.ComicCreate.as_view(), name='comics_create'),
    path('comics/<int:pk>/update/', views.ComicUpdate.as_view(), name='comics_update'),
    path('comics/<int:pk>/delete/', views.ComicDelete.as_view(), name='comics_delete'),
    path('genres/', views.GenreList.as_view(), name='genres_index'),
    path('genres/<int:pk>/', views.GenreDetail.as_view(), name='genres_detail'),
    path('genres/create/', views.GenreCreate.as_view(), name='genres_create'),
    path('genres/<int:pk>/update/', views.GenreUpdate.as_view(), name='genres_update'),
    path('genres/<int:pk>/delete/', views.GenreDelete.as_view(), name='genres_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]