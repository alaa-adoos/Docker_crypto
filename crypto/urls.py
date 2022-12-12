from django.urls import path
from .views import CryptoListView,CryptoDetailView

urlpatterns = [
      path('', CryptoListView.as_view(), name='crypto_list'),
      path('<int:pk>/', CryptoDetailView.as_view(), name='crypto_detail'),
#     path('create/', CreateView.as_view(), name='_create'),
#     path('<int:pk>/update/', UpdateView.as_view(), name='_update'),
#     path('<int:pk>/delete/', DeleteView.as_view(), name='_delete'),
]