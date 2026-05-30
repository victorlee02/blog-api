from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.BlogListCreateView.as_view()),
    path('blogs/<int:pk>/', views.BlogDetailView.as_view()),
    path('blogs/<int:pk>/comments/', views.CommentListCreateView.as_view()),
]
