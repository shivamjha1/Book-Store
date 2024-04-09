from django.shortcuts import render

from .models import Book,Author,Address
books=Book.objects.all()
# Create your views here.
def index(request):
    return render(request,"store/index.html",{
        "books":books
    })
def book_detail(request,slug):
    book=Book.objects.get(slug=slug)
    return render(request,"store/book_detail.html",{
         "book":book
    })
def student_detail(request):
    pass