from django.shortcuts import render, redirect
from .models import Book
from login.models import User
from django.contrib import messages

def render_books_home(request):
	if request.session['logged_on']:
		context = {
			'books': Book.objects.all().order_by('-created_at'),
			'user': User.objects.get(id=request.session['user_id'])
		}
		return render(request, 'books_home.html', context)
	else:
		return redirect('/')

def add_book(request):
	if request.method == "POST":
		errors = Book.objects.book_validator(request.POST)
		if len(errors) > 0:
			for key, value in errors.items():
				messages.error(request, value, extra_tags="add_book")
			return redirect("/")
		else:
			Book.objects.create(title=request.POST['title'], desc=request.POST['desc'], uploaded_by=User.objects.get(id=request.session['user_id']))
			Book.objects.last().users_who_like.add(User.objects.get(id=request.session['user_id']))  
			return redirect('/')

def render_book_page(request, id):
	if request.session['logged_on']:
		context = {
			'book': Book.objects.get(id=id),
			'user': User.objects.get(id=request.session['user_id'])
		}
		return render(request, 'book_page.html', context)
	return redirect('/')

def update_book(request, id):
	if request.method == "POST":
		errors = Book.objects.book_validator(request.POST)
		if len(errors) > 0:
			for key, value in errors.items():
				#edit
				messages.error(request, value, extra_tags="add_book")
		else:
			book = Book.objects.get(id=id)
			book.title = request.POST['title']
			book.desc = request.POST['desc']
			book.save()
	return redirect(f"/books/{id}")

def delete_book(request, id):
	if request.session['user_id'] == Book.objects.get(id=id).uploaded_by.id:
		Book.objects.get(id=id).delete()
	return redirect('/')

#doubles as unfavorite method
def add_favorite(request, id):
	if request.session['logged_on']:
		if User.objects.get(id=request.session['user_id']) in Book.objects.get(id=id).users_who_like.all():
			Book.objects.get(id=id).users_who_like.remove(User.objects.get(id=request.session['user_id']))
		else:
			Book.objects.get(id=id).users_who_like.add(User.objects.get(id=request.session['user_id']))
	return redirect('/')

	