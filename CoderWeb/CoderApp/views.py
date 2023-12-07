from django.shortcuts import render,redirect
from .forms import EntradaForm,ComediaForm,CienciaficcionForm
from. models import Terror




def index(request):
    return render(request,'index.html')

def terror(request):
    return render(request,'terror.html')

def comedia(request):
    return render(request,'comedia.html')

def ciencia_ficcion(request):
    return render(request,'cienciaficcion.html')

def formulario_terror(request):
    if request.method == 'POST':
        miformulario = EntradaForm(request.POST) #AQUI MANEJA LA INFORMACION DEL HTML 
        if miformulario.is_valid(): #Valido  
            terror = miformulario.save()
            return redirect('/Cinefilos/') #VUELVO AL INICIO
    else:
        miformulario = EntradaForm()  #FORMULARIO VACIO PARA CONSTRUIR EL HTLM
    return render(request,'terror.html',{'form':miformulario})

def formulario_cienciaficcion(request):   #Formulario de ciencia ficcion
    if request.method == 'POST':
        miformulario = CienciaficcionForm(request.POST)  
        if miformulario.is_valid(): 
            terror = miformulario.save()
            return redirect('/Cinefilos/') 
    else:
        miformulario = CienciaficcionForm() 
    return render(request,'cienciaficcion.html',{'form':miformulario})

def formulario_comedia(request):           #Formulario de comedia
    if request.method == 'POST':
        miformulario = ComediaForm(request.POST)
        if miformulario.is_valid(): 
            terror = miformulario.save()
            return redirect('/Cinefilos/') 
    else:
        miformulario = ComediaForm()  
    return render(request,'comedia.html',{'form':miformulario})



    
def lista_terror(request):
    lista_de_terror= Terror.objects.all()
    # Pasa los objetos del modelo al contexto
    return render(request,"lista-terror.html",{'lista_de_terror':lista_de_terror})
