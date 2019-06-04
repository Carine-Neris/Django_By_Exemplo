from django.urls import path
from . import views 
from .feeds import LatestPostsFeed

app_name = 'blog'
urlpatterns = [
    # post views
    path('', views.post_list, name='post_list'),
    # path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail,
         name='post_detail'),
    path('<int:post_id>/share/',
         views.post_share, name='post_share'),
    path('tag/<slug:tag_slug>/',
         views.post_list, name='post_list_by_tag'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('filtro/', views.post_list_draft, name='post_list_draft'),
    path('comentarios/', views.comentario_detalhe, name='comentario_detalhe'),
    path('<slug:post>/', views.slug_post, name='slug_post'),
    path('detalhe', views.view_detalhe, name='view_detalhe'),

    path('post/tags/<slug:tag_slug>/', views.retorna_post, name='retorna_post'),
]