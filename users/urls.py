# Djando
from django.urls import path
# Views
from users import views

urlpatterns = [

    #Management
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('me/profile/', views.UpdateProfileView.as_view(), name='update'),

    #Posts
    path(
        route='profile/<str:username>/', # la url será el username
        view=views.UserDetailView.as_view(), # vista basada en clases
        name='detail'
    ),
]
