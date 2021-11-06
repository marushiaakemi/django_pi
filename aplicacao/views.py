from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView
from aplicacao.forms import MeuFormulario
from .models import Formulario, Post

class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post

def form_django(request):
    if request.method == "GET":
        pessoas = Formulario.objects.all()

        form = MeuFormulario()
        context = {
            'form': form,
            'pessoas':pessoas,
        }
        return render (request, "aplicacao/formulario.html", context=context)    

    elif request.method == 'POST':
        form = MeuFormulario(request.POST)

        if form.is_valid():
            form.save()
            return redirect('.')
        else:
            pessoas = Formulario.objects.all()
            
            context = {
                'form':form,
                'pessoas':pessoas,
            }
            return render (request, "aplicacao/formulario.html", context=context)    

def update(request, pessoa_id):
    if request.method == 'GET':
        pessoas = Formulario.objects.all()
        pessoa = Formulario.objects.filter(id=pessoa_id).first()
        form = MeuFormulario(instance=pessoa)
        context = {
                'form':form,
                'pessoas':pessoas,
        }
        return render (request, "aplicacao/formulario.html", context=context)    

    elif request.method == 'POST':
        pessoa = Formulario.objects.filter(id=pessoa_id).first()
        form = MeuFormulario(request.POST, instance=pessoa)

        if form.is_valid():
            form.save()
            return redirect('.')
        else:
            pessoas = Formulario.objects.all()
            
            context = {
                'form':form,
                'pessoas':pessoas,
            }
            return render (request, "aplicacao/formulario.html", context=context) 

def delete_view(request, pessoa_id):
    if request.method == 'GET':
        pessoas = Formulario.objects.all()
        pessoa = Formulario.objects.filter(id=pessoa_id).first()
        form = MeuFormulario(instance=pessoa)
        context = {
                'form':form,
                'pessoas':pessoas,
        }
        return render (request, "aplicacao/formulario.html", context=context)    

    elif request.method == 'POST':
        pessoa = Formulario.objects.filter(id=pessoa_id).first()
        form = MeuFormulario(request.POST, instance=pessoa)

        if form.is_valid():
            pessoa.delete()
            pessoas = Formulario.objects.all()
            form = MeuFormulario()
            
            context = {
                'form':form,
                'pessoas':pessoas,
            }
            return render (request, "aplicacao/formulario.html", context=context)
        else:
            pessoas = Formulario.objects.all()
            
            context = {
                'form':form,
                'pessoas':pessoas,
            }
            return render (request, "aplicacao/formulario.html", context=context)          

