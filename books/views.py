from django.shortcuts import render
from django.utils import timezone
from .models import Book

# Create your views here.
def book_list(request):
	books = Book.objects.order_by('start_date')
	return render(request, 'books/book_list.html', {'books':books})
