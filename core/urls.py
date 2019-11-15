from django.urls import path
from .views import CasasListView,CasasDetailView,CasasCreate,CasasUpdate,CasasDelete
from .views import DepartamentoListView,DepartamentoDetailView,DepartamentoCreate,DepartamentoUpdate,DepartamentoDelete
from .views import TerrenosListView,TerrenosDetailView,TerrenosCreate,TerrenosUpdate,TerrenosDelete
from .views import GaleriaListView,GaleriaCreate,GaleriaUpdate,GaleriaDelete
from .views import QuienesSomosPageView,ContactoPageView,IndexPageView

urlpatterns = [
    
    path('', IndexPageView.as_view(), name='home'),
    path("casas/", CasasListView.as_view(), name="casas"),
    path("casas/<int:pk>/", CasasDetailView.as_view(), name="casa"),
    path("casas/create/", CasasCreate.as_view(), name="casa_new"),
    path("casas/update/<int:pk>/", CasasUpdate.as_view(), name="casa_update"),
    path("casas/delete/<int:pk>/", CasasDelete.as_view(), name="casa_delete"),
    path("departamento/", DepartamentoListView.as_view(), name="deptos"),
    path("departamento/<int:pk>/", DepartamentoDetailView.as_view(), name="depto"),
    path("departamento/create/", DepartamentoCreate.as_view(), name="depto_new"),
    path("departamento/update/<int:pk>/", DepartamentoUpdate.as_view(), name="depto_update"),
    path("departamento/delete/<int:pk>/", DepartamentoDelete.as_view(), name="depto_delete"),
    path("terrenos/", TerrenosListView.as_view(), name="terrenos"), 
    path("terrenos/<int:pk>/", TerrenosDetailView.as_view(), name="terre"),
    path("terrenos/create/", TerrenosCreate.as_view(), name="terreno_new"),
    path("terrenos/update/<int:pk>/", TerrenosUpdate.as_view(), name="terreno_update"),
    path("terrenos/delete/<int:pk>/", TerrenosDelete.as_view(), name="terreno_delete"),
    path("contacto/", ContactoPageView.as_view(), name="contacto"),
    path("galeria/", GaleriaListView.as_view(), name="galeria"),
    path("galeria/create/", GaleriaCreate.as_view(), name="galeria_new"),
    path("galeria/update/<int:pk>/", GaleriaUpdate.as_view(), name="galeria_update"),
    path("galeria/delete/<int:pk>/", GaleriaDelete.as_view(), name="galeria_delete"),
    path("quienes-somos/", QuienesSomosPageView.as_view(), name="quienes_somos"),

]

