from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contato
from .forms import ContatoForm

def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def education(request):
    return render(request,'education.html')
def portfolio(request):
    return render(request,'portfolio.html')

def contact(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            contato = Contato(name=name, email=email, message=message)
            contato.save()

            messages.success(request, 'Mensagem enviada com sucesso!')
            return render(request, 'success.html')  # Renderiza a página success.html

    else:
        form = ContatoForm()

    return render(request, 'contact.html', {'form': form})
def success(request):
    return render(request, 'success.html')