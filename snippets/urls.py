from django.urls import path

from . import views

app_name = 'snippets'

urlpatterns = [
    path('', views.SnippetList.as_view(), name='list'),
    path('tag/<str:tag>/', views.SnippetList.as_view(), name='by-tag'),
    path('create/', views.SnippetCreate.as_view(), name='create'),
    path('<int:pk>/', views.SnippetDetail.as_view(), name='detail'),
    path('<int:pk>/update/', views.SnippetUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', views.SnippetDelete.as_view(), name='delete'),
]
