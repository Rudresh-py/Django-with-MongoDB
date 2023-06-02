from django.urls import path
from app.views import RegisterView, UsersView, ProductCreate

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('users/', UsersView.as_view(), name="users"),
    path('product/create/', ProductCreate.as_view(), name="createproduct"),
    path('product/create/<str:pk>/', ProductCreate.as_view(), name="updateproduct")

]
