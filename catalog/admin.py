from django.contrib import admin
from .models import Author, Genre, Book, BookInstance


# Register your models here.
# Define the admin classes and register them using the decorator

class BooksInline(admin.TabularInline):
    # Add inline Book editing functionality for Author
    model = Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    # Change listing order
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

    # Change which fields are displayed and how they're laid out
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

    # Inline listing for books by author
    inlines = [BooksInline]


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Can't specify genre field in `list_display` because it's a ManyToManyField
    # Solution: display_genre function in Book model
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]


# Genre doesn't have an admin class
admin.site.register(Genre)


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )
