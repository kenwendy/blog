from django.shortcuts import render

# Create your views here.
from book.models import Book


def book(request):
    books = Book.objects.all()
    return render(request, 'book/book.html', {'books':books})