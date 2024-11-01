from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from django.db.models import Q

# Create your views here.
def index(request):
    books=Book.objects.all()        
        
    return render(request,'index.html',{'books': books})

def modif(request, book_id):
    # Récupérer le livre à modifier
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        # Si le formulaire est soumis, mettez à jour les détails du livre
        book.title = request.POST['title']
        book.auteur = request.POST['auteur']
        book.categorie = request.POST['categorie']
        book.disponibilite = request.POST['disp']
        book.save()
        return redirect('index')  # Redirigez vers la page d'accueil ou une autre page

    # Si c'est une requête GET, affichez le formulaire de modification
    context = {
        'book': book
    }
    return render(request, 'modifier.html', context)


def mod_details(request,book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        # Si le formulaire est soumis, mettez à jour les détails du livre
        book.title = request.POST['title']
        book.auteur = request.POST['auteur']
        book.categorie = request.POST['categorie']
        book.date = request.POST['date']
        book.isbn = request.POST['isbn']
        book.resume = request.POST['resume']
        book.save()
        return redirect('index')  # Redirigez vers la page d'accueil ou une autre page

    # Si c'est une requête GET, affichez le formulaire de modification
    
    return render(request,"mod_details.html",{'book':book})

def details(request,book_id):
    try:

        book = get_object_or_404(Book, id=book_id)
    except Exception as e:
        print(f"Erreur lors afficher details : {e}")

    return render(request,'details.html',{'book':book})


def supp(request, book_id):
    try:
        # Récupérer l'objet Book par ID
        book = get_object_or_404(Book, id=book_id)
        book.delete()  # Supprimer l'objet
        return redirect('index')  # Rediriger vers la page d'index après la suppression
    except Exception as e:
        print(f"Erreur lors de la suppression du livre : {e}")
        return redirect('index')

def ajouter(request):
    books = Book.objects.all()  # Récupère tous les livres existants
    try:
        if request.method == "POST":
            title = request.POST.get('title')
            auteur = request.POST.get('auteur')
            categorie = request.POST.get('categorie')
            disponibilite = "Disponible"

            # Crée un nouvel objet Book sans écraser la liste `books`
            new_book = Book(title=title, auteur=auteur, categorie=categorie, disponibilite=disponibilite)
            new_book.save()

            # Recharge la liste des livres pour inclure le nouveau livre ajouté
            books = Book.objects.all()
            return render(request, 'index.html', {'books': books})

    except Exception as e:
        print(f"Erreur lors de la création de l'utilisateur : {e}") 

    return render(request, 'index.html', {'books': books})



def rech(request):
    books = Book.objects.all()  # Récupérer tous les livres par défaut
    recherche = None  # Initialiser la variable recherche

    if request.method == "POST":
        recherche = request.POST.get('rech')  # Récupérer la valeur de recherche

        if recherche:
            # Filtrer les livres dont le titre contient la valeur recherchée
            books = books.filter(Q(title__icontains=recherche) | Q(Auteur__icontains=recherche))

    return render(request, 'index.html', {'books': books, 'recherche': recherche})