from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils import timezone
from django.urls import reverse_lazy
from .models import Casa
from .models import Departamento
from .models import Terreno
from .models import  Galeria
# Create your views here.

# mixim para poder redireccionar la pagina si el usuario no esta
# autenticado para cuando apriete el boton de arriendo o venta
# tambien se podria usar el decorador login_required 

#class LoginRequired(object):
    #def dispatch(self,request,*args,**kwargs):
        #if not request.user.is_authenticated:
            #return redirect(reverse_lazy('login'))
        #return super(StaffRequired,self).dispatch(request,*args,**kwargs)
############################################################################

#CRUD CASAS 
class CasasListView(ListView):
    model = Casa
    template_name = "core/casa_list.html"
    paginate_by = 6

@method_decorator(login_required(login_url='login') ,name = 'dispatch' )
class CasasDetailView(DetailView):
    model = Casa

@method_decorator(staff_member_required(login_url='login'), name = 'dispatch')
class CasasCreate(CreateView):
    model = Casa
    fields = [
        'autor',
        'titulo',
        'descripcion',
        'imagen',
        'direccion',
        'ciudad',
        'precio',
        'cant_habitaciones',
        'cant_baños',
        'metros_2',
        'patio',
        'tipo_contacto',
        'created_date',
        'published_date',
        'destacado'
    ]
    success_url = reverse_lazy('casas')

@method_decorator(staff_member_required(login_url='login'), name = 'dispatch')
class CasasUpdate(UpdateView):
    model = Casa
    fields = [
        'autor',
        'titulo',
        'descripcion',
        'imagen',
        'direccion',
        'ciudad',
        'precio',
        'cant_habitaciones',
        'cant_baños',
        'metros_2',
        'patio',
        'tipo_contacto',
        'created_date',
        'published_date',
        'destacado'
    ]
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('casa_update',args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required(login_url='login'), name = 'dispatch')
class CasasDelete(DeleteView):
    model = Casa
    success_url = reverse_lazy('casas')

#CRUD DEPARTAMENTOS 
class DepartamentoListView(ListView):
    model = Departamento
    template_name = "core/departamento_list.html"
    paginate_by = 6

class DepartamentoDetailView(DetailView):
    model = Departamento

@method_decorator(staff_member_required(login_url='login'), name = 'dispatch')
class DepartamentoCreate(CreateView):
    model = Departamento
    fields = [
        'autor',
        'titulo',
        'descripcion',
        'imagen',
        'direccion',
        'num_piso',
        'ciudad',
        'precio',
        'cant_habitaciones',
        'cant_baños',
        'metros_2',
        'tipo_contacto',
        'created_date',
        'published_date',
        'destacado'
    ]
    success_url = reverse_lazy('deptos')

@method_decorator(staff_member_required(login_url='login'), name = 'dispatch')
class DepartamentoUpdate(UpdateView):
    model = Departamento
    fields = [
        'autor',
        'titulo',
        'descripcion',
        'imagen',
        'direccion',
        'num_piso',
        'ciudad',
        'precio',
        'cant_habitaciones',
        'cant_baños',
        'metros_2',
        'tipo_contacto',
        'created_date',
        'published_date',
        'destacado'
    ]
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('depto_update',args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required(login_url='login'), name = 'dispatch')
class DepartamentoDelete(DeleteView):
    model = Departamento
    success_url = reverse_lazy('deptos')

#CRUD TERRENOS 
class TerrenosListView(ListView):
    model = Terreno
    template_name = "core/terreno_list.html"
    paginate_by = 6

class TerrenosDetailView(DetailView):
    model = Terreno

@method_decorator(staff_member_required(login_url='login'), name = 'dispatch')
class TerrenosCreate(CreateView):
    model = Terreno
    fields = [
        'autor',
        'titulo',
        'descripcion',
        'imagen',
        'direccion',
        'ciudad',
        'precio',
        'metros_2',
        'tipo_contacto',
        'created_date',
        'published_date',
        'destacado'
    ]
    success_url = reverse_lazy('terrenos')

@method_decorator(staff_member_required(login_url='login'), name = 'dispatch')
class TerrenosUpdate(UpdateView):
    model = Terreno
    fields = [
        'autor',
        'titulo',
        'descripcion',
        'imagen',
        'direccion',
        'ciudad',
        'precio',
        'metros_2',
        'tipo_contacto',
        'created_date',
        'published_date',
        'destacado'
    ]
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('terreno_update',args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required(login_url='login'), name = 'dispatch')
class TerrenosDelete(DeleteView):
    model = Terreno
    success_url = reverse_lazy('terrenos')

#CRUD GALERIA

class GaleriaListView(ListView):
    model = Galeria
    template_name = "core/galeria_list.html"
    paginate_by = 6

@method_decorator(staff_member_required(login_url='login'), name = 'dispatch')
class GaleriaCreate(CreateView):
    model = Galeria
    fields = [
        'titulo',
        'imagen',
        'created_date',
        'published_date',
    ]
    success_url = reverse_lazy('galeria')

@method_decorator(staff_member_required(login_url='login'), name = 'dispatch')
class GaleriaUpdate(UpdateView):
    model = Galeria
    fields = [
        'titulo',
        'imagen',
        'created_date',
        'published_date',
    ]
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('galeria_update', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required(login_url='login'), name = 'dispatch')
class GaleriaDelete(DeleteView):
    model = Galeria
    success_url = reverse_lazy('galeria')

    #---------FIN GALERIA--------------


class ContactoPageView(TemplateView):
    template_name = "core/contacto.html"

class QuienesSomosPageView(TemplateView):
    template_name = "core/quienes-somos.html"

class IndexPageView(TemplateView):

    template_name = "core/index.html"

    def get(self,request,*args, **kwargs):
        casas = Casa.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        deptos = Departamento.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        terres = Terreno.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        return render(request, self.template_name, {'casas': casas,'deptos': deptos,'terres': terres})





