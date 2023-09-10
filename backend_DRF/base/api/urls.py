from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('registro/', views.RegisterView.as_view(), name='registrar_usuario'),
    path('espacio/', views.espacio, name='espacio_general'),
    path('espacio/<int:pk>/', views.detalle_espacio, name='espacio_detalle'),
    path('espacio/<int:pk>/participaciones/', views.participaciones_espacios, name='invitar_a_espacio'),
    path('tablero/', views.tablero, name='tablero_general'),
    path('tablero/<int:pk>/', views.detalle_tablero, name='tablero_detalle'),
    path('lista/', views.lista, name='lista_general'),
    path('lista/<int:pk>/', views.detalle_lista, name='lista_detalle'),
    path('tarjeta/', views.tarjeta, name='tarjeta_general'),
    path('tarjeta/<int:pk>/', views.detalle_tarjeta, name='tarjeta_detalle'),
    path('comentario/', views.comentario, name='post_comentario'),
    path('respuesta/', views.respuesta, name='post_respuesta')
]