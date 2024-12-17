from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def Erro(request, exception):
    try:
        return render(request, 'erro.html', status=404)
    except Exception as e:
        print(f"Erro ao renderizar o template: {e}")
        return render(request, 'default_error.html', status=500)