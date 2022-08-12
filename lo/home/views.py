from re import I
from django.shortcuts import render,redirect
from books.models import book_list
from django.http.response import JsonResponse
from django.db.models.query_utils import Q

# Create your views here.

def index(request):
    book = book_list.objects.all()
    return render(request,"index.html",{'book':book})
  
        
        
def serach(request):
    if 'term' in request.GET:
        s_e = request.GET['term']
        print(s_e)
        ob_s=book_list.objects.filter(Q(b_name__istartswith=s_e))
        ali=[]
        for i in ob_s:
            ali.append(i.b_name)
        return JsonResponse(ali,safe=False)
    return redirect("/")