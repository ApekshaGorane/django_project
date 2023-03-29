from django.db import models

class AppManager(models.Manager):
    def all_price_in_descending_order(request):
        return super().order_by('-price')

    def all_price_in_ascending_order(request):
        return super().order_by('price')

    def sort_by_authorname_ATOZ(request):
        return super().order_by('author_name')

    def sort_by_authorname_ZTOA(request):
        return super().order_by('-author_name')
    
    def sort_by_bookname_ATOZ(request):
        return super().order_by('book_name')
    
    def sort_by_bookname_ZTOA(request):
        return super().order_by('-book_name')
    
    def sort_by_id_ltoh(request):
        return super().order_by('id')
    
    def sort_by_id_htol(request):
        return super().order_by('-id')
    
   


   