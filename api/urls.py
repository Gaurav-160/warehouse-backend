from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path
from api import views

urlpatterns = [
    path("token/", views.MyTokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("register/", views.RegisterView.as_view()),
    path("google-auth/", views.GoogleView.as_view()),
    path("dashboard/", views.dashboard),
    path('home/', views.HomeView.as_view(), name='home')
]