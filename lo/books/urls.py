from django.urls import path,include
from books import views


urlpatterns = [
    path('',views.bookdeta),
    path('comment/',views.bookcomment,name='comment'),
    path('searchbook/',views.serbook,name='sear_book'),
]
