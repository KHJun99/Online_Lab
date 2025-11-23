from django.contrib import admin
from .models import Author, Book, AuthorSubscription

# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nickname', 'user')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'genre')
    list_filter = ('genre', 'author')


@admin.register(AuthorSubscription)
class AuthorSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'user')