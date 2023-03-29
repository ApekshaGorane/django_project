from django.urls import path
from app1 import views

urlpatterns = [
    path('add/',views.add),
    path('delete/<int:tid>',views.delete),
    path('update/<int:tid>',views.update),
    path('htol',views.htol),
    path('ltoh',views.ltoh),
    path('catfilter/<str:cat>',views.catfilter),
    path('',views.home),
    path('bookname_ATOZ',views.bookname_ATOZ),
    path('bookname_ZTOA',views.bookname_ZTOA),
    path('authorname_ATOZ',views.authorname_ATOZ),
    path('authorname_ZTOA',views.authorname_ZTOA),
    path('id_htol',views.id_htol),
    path('id_ltoh',views.id_ltoh),
    path('register/',views.register),
    path("errorshow/",views.errorshow)
   
]

