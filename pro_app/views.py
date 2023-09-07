from django.shortcuts import render
from django.http import HttpResponse
from pro_app.models import About
from pro_app.models import Demande

# Create your views here.

def index(request):
    abouts = About.objects.all()
    if request.method == "POST":
        demande = Demande()
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        societe = request.POST.get('societe')
        message = request.POST.get('message')
        
        demande.nom = nom
        demande.email = email
        demande.societe = societe
        demande.message = message
        demande.prenom = prenom

        demande.save()
        return HttpResponse("<h3>Votre demande a bien ete soumise !!!")
    
    return render(request, 'index.html', {'abouts':abouts})

def services(request):
    return render(request, 'services.html')

