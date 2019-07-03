from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Book

# Create your views here.
def book_list(request):
	books = Book.objects.order_by('start_date')
	return render(request, 'books/book_list.html', {'books':books})

def book_detail(request, pk):
	book = get_object_or_404(Book, pk=pk)
	return render(request, 'books/book_detail.html', {'book': book})
