from django.db import models
from login.models import User

class BookManager(models.Manager):
	def book_validator(self, post_data):
		errors = {}
		if len(post_data['title']) < 1:
			errors['title'] = 'Title is required'
		if len(post_data['desc']) < 5:
			errors['desc'] = 'Description must be at least 5 characters'
		return errors
		
class Book(models.Model):
	title = models.CharField(max_length=255)
	desc = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	uploaded_by = models.ForeignKey(User, related_name="books", on_delete=models.CASCADE)
	users_who_like = models.ManyToManyField(User, related_name='liked_books')
	objects = BookManager()