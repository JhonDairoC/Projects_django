from django.urls import path
from .views import ProducListApiView, ProducDetailApiView, ClasificApiView, IdClasificApiView

urlpatterns = [
    path('', ProducListApiView.as_view(), name="Produc_list"),
    path('<int:produc_id>/', ProducDetailApiView.as_view(), name="Produc_detail"),
    path('<str:produc_clasific>/', ClasificApiView.as_view(), name="Produc_list"),
    path('<str:produc_clasific>/<int:id_clasific>/', IdClasificApiView.as_view(), name="Produc_detail")
]