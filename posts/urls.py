#Django
from django.urls import path
# Views
from posts import views

urlpatterns = [
    #se puede hacer de estas dos maneras
    path(
        route='',
        view=views.PostsFeedView.as_view(),
        name='feed'),

    path('new/', views.CreatePostView.as_view(), name='create'),

    path(
        route='posts/<int:pk>/',
        view=views.PostDetailView.as_view(),
        name='detail'
    ),
]

