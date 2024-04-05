from django.contrib import admin
from .models import Book,Student

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("title",)}
    list_filter=("author","rating",)
    list_display=("title","author",)

# Register your models here.
admin.site.register(Book,BookAdmin)

admin.site.register(Student)