from django.shortcuts import render, redirect
from .models import Book

def render_books_home(request):
	if request.session['logged_on']:
		context = {
			'books': Book.objects.all().order_by('-created_at')
		}
		return render(request, 'books_home.html', context)
	else:
		return redirect('/')