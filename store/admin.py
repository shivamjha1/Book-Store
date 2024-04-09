from django.contrib import admin
from .models import Book,Student,Author,Address

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("title",)}
    list_filter=("author","rating",)
    list_display=("title","author",)

class AuthorAdmin(admin.ModelAdmin):
    list_filter=("first_name",)


# Register your models here.
admin.site.register(Book,BookAdmin)

admin.site.register(Student)

admin.site.register(Author,AuthorAdmin)

admin.site.register(Address)
