from django.shortcuts import render, redirect
from .forms import FormUser
from django.contrib.auth.decorators import login_required
from .models import Noticia, Comentario
# Create your views here.

def index(i):
    noticias = Noticia.objects.order_by('titulo')
    dados = {'Noticias':noticias}
    return render(i,'base/index.html', dados)

def registo(i):
    msg=''
    if i.method =='POST':
        form = FormUser(i.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            msg='Dados incorretos, por favor tente outra vez'
    return render(i, 'base/registo.html', {'form':FormUser(),'msg':msg})

def detalhe(i, Noticia_id):
    noticia = Noticia.objects.get(pk=Noticia_id)
    comentarios = Comentario.objects.filter(noticia=Noticia_id)
    dados = {'Noticia':noticia,'Comentario':comentarios}
    return render(i, 'base/detalhe.html', dados)

@login_required
def comentario(i, Noticia_id):
    noticia = Noticia.objects.get(pk=Noticia_id)
    return render(i, "base/comentario.html", {'Noticia':noticia})

  
@login_required   
def fim(i):    
    if i.method=='POST':
        noti_id = i.POST['id_noticia']
        noti = Noticia.objects.get(pk=noti_id)
        txt = i.POST['texto_input']
        comentar = Comentario.objects.create(
            user = i.user,
            noticia = noti,
            texto = txt
            )
        comentar.save()
    return render(i, 'base/fim.html')



 
    
