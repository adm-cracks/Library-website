from django.shortcuts import render
from .models import book_list

# Create your views here.

def bookdeta(request):
    b_id = request.GET['id']
    book_deta = book_list.objects.get(id=b_id)
    return render(request,'product.html',{'bo_de':book_deta})