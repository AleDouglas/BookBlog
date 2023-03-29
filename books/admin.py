from django.contrib import admin
from .models import Book, Review



class ReviewInline(admin.TabularInline): # new
    model = Review

class BookAdmin(admin.ModelAdmin): # new
    inlines = [ReviewInline]
    list_display = ("title", "author", "price",)

    
admin.site.register(Book, BookAdmin) # new