from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Book
from .forms import BookForm
from django.shortcuts import redirect

# Create your views here.
def book_list(request):
	books = Book.objects.order_by('start_date')
	return render(request, 'books/book_list.html', {'books':books})

def book_detail(request, pk):
	book = get_object_or_404(Book, pk=pk)
	return render(request, 'books/book_detail.html', {'book': book})

def book_new(request):
	if request.method == "POST":
		form = BookForm(request.POST)
		if form.is_valid():
			book = form.save(commit=False)
			book.save()
			return redirect('book_detail', pk=book.pk)
	else:
		form = BookForm()
	return render(request, 'books/book_edit.html', {'form': form})

def book_edit(request, pk):
	book = get_object_or_404(Book, pk=pk)
	if request.method=="POST":
		form = BookForm(request.POST, instance=book)
		if form.is_valid():
			book = form.save(commit=False)
			book.save()
			return redirect('book_detail', pk=book.pk)
	else:
		form = BookForm(instance=book)
	return render(request, 'books/book_edit.html', {'form':form})
			
