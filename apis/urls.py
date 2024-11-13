from django.urls import path
from .views import RegisterView, LoginView, CategoryView,ProductView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


    # users categories
    path('categories/', CategoryView.as_view(), name='category'),
    path('categories/<int:pk>/', CategoryView.as_view(), name='one-category'),

# users categories
    path('product/', ProductView.as_view(), name='category'),
    path('product/<int:pk>/', ProductView.as_view(), name='one-category'),

]
