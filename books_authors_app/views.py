from django.shortcuts import render,redirect
from .models import Book,Publisher
# Create your views here.
def index(request):   
    context = {
        "book" : Book.objects.all(),
    }
    return render(request,"book.html",context)

def show(request):
    context = {
        "pub" : Publisher.objects.all(),       
    }
    return render(request,"author.html",context)

def books(request):
    title = request.POST['title']
    desp = request.POST['description']
    Book.objects.create(title = title, description = desp)   
    return redirect('/')

def authors(request):
    firstname = request.POST['fname']
    lastname = request.POST['lname']
    name = firstname + ' ' + lastname
    note = request.POST['note']
    Publisher.objects.create(name = name, notes = note)   
    return redirect('/authors')

def book_des(request, id):
    if 'id' not in request.session:
        request.session['id'] = 0
    this_book = Book.objects.get(id = id)
    request.session['id'] = id
    context = {
        "book" : this_book,
        "authors": this_book.publishers.all(),
        "pub" : Publisher.objects.all(),
    }
    return render(request,"book_des.html",context)

def author_add(request):
    author = request.POST['auth']
    id = request.session['id']
    print(id)
    this_book = Book.objects.get(id = id)    
    this_publisher = Publisher.objects.get(name = author)
    print(this_publisher)
    this_publisher.books.add(this_book)
    this_book.publishers.add(this_publisher)
    print(this_book.publishers.name)
    return redirect('id_detail',id = id)

def auth_des(request, id):
    if 'id' not in request.session:
        request.session['id'] = 0
    this_auth = Publisher.objects.get(id = id)
    request.session['id'] = id
    context = {
        "auth" : this_auth,
        "books": this_auth.books.all(),
        "book" : Book.objects.all(),
    }
    return render(request,"author_des.html",context)

def book_add(request):
    book = request.POST['book']
    id = request.session['id']
    this_book = Book.objects.get(title = book)    
    this_publisher = Publisher.objects.get(id = id)
    this_publisher.books.add(this_book)
    this_book.publishers.add(this_publisher)
    return redirect('author_detail',id = id)