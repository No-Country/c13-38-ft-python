from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('registro/', views.RegisterView.as_view(), name='registrar_usuario'),
    path('tablero/', views.tablero, name='tablero_general'),
    path('tablero/<int:pk>/', views.detalle_tablero, name='tablero_detalle'),
    path('tablero/<int:pk>/participaciones/',
        views.participaciones_tableros, name='invitar_a_tablero')
]