from itertools import product
from django.shortcuts import render,redirect
from .models import book_list
from .models import book_comment
from django.db.models.query_utils import Q

# Create your views here.

def bookdeta(request):
    b_id = request.GET['id']
   
    book_deta = book_list.objects.get(id=b_id)
    return render(request,'product.html',{'bo_de':book_deta})

#serch
def serbook(request):
    
    se_el = request.POST['serbk']
    print('search',se_el)
    #book_deta = book_list.objects.get(Q(b_name__istartswith=se_el))
   
    if book_list.objects.filter(b_name=se_el):
        book_deta = book_list.objects.get(b_name=se_el)
        return render(request,'product.html',{'bo_de':book_deta})
    else:
        print("not found   book")
        book_deta = "sorry cannot find it"
        return render(request,'product.html',{'bo':book_deta})




def bookcomment(request):
    us_name = request.POST['uname']
    b_com = request.POST['comt']
    u_email = request.POST['uemai']
    b_id = request.POST['bid']
   
    dx = book_comment.objects.filter(product_id=b_id)
    print(dx)
    ali=[]
   
    for i in dx:
        ali.append(i.emi)
   
    if  u_email not in ali: 
        com_st = book_comment.objects.create(u_name=us_name,emi=u_email,com_area=b_com,product_id=b_id)
        com_st.save();
    return redirect('/product/?id='+b_id)