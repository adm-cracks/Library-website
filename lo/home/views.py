from django.shortcuts import render
from books.models import book_list

# Create your views here.

def index(request):
    book = book_list.objects.all()
    return render(request,"index.html",{'book':book})