from django.shortcuts import render

def home(request):
    return render(request, 'ERP/home.html')  # Caminho relativo ao diretório templates
