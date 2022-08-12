from django.urls import path,include
from home import views

urlpatterns = [
    path('',views.index,name='homepage'),
    path('serach/',views.serach,name='ser'),
]
