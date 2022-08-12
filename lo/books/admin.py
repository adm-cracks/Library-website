from django.contrib import admin
from .models import book_list
from .models import book_comment

# Register your models here.

admin.site.register(book_list)
admin.site.register(book_comment)
