from django.urls import path
from .views import (
    ArticleListView,
    ArticleDeleteView,
    ArticleUpdateView,
    ArticleDetailtView,
    ArticleCreateView,
)

urlpatterns = [
    path('<int:pk>/', ArticleDetailtView.as_view(), name="article_details"),
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name="article_edit"),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name="article_delete"),
    path('new/', ArticleCreateView.as_view(), name="article_new"),
    path('', ArticleListView.as_view(), name='article_list'),
]
