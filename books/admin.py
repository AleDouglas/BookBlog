from django.contrib import admin
from .models import Book, Review, Category


class BookInLine(admin.TabularInline):
    model = Book

class CategoryAdmin(admin.ModelAdmin):
    inlines = [BookInLine]
    list_display = ("title", )

admin.site.register(Category, CategoryAdmin)


class ReviewInline(admin.TabularInline): 
    model = Review

class BookAdmin(admin.ModelAdmin): 
    inlines = [ReviewInline]
    
    list_display = ("title", "category","author",)


admin.site.register(Book, BookAdmin)


