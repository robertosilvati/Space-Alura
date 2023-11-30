from django.urls import path
from galeria.views import index

# Todas as rotas relcionadas a geleria.
urlpatterns = [
    path('', index)
]