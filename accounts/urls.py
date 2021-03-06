from accounts.api.viewSet import RegisterAPI
from django.urls import path, include
from knox import views as knox_views
from accounts.api.viewSet import LoginAPI, ShowUsers

urlpatterns = [
    path('api/v1/register/', RegisterAPI.as_view(), name='register'),
    path('api/v1/login/', LoginAPI.as_view(), name='login'),
    path('api/v1/user/<int:pk>/', ShowUsers.as_view(), name='user-detail'), # verificar
    path('api/v1/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/v1/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),

]