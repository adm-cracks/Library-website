from django.urls import path,include
from books import views


urlpatterns = [
    path('',views.bookdeta,name='sera2'),
    path('comment/',views.bookcomment,name='comment'),
    path('searchbook/',views.serbook,name='sear_book'),
]
