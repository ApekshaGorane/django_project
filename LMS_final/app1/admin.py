from django.contrib import admin
from app1.models import BookModel
# Register your models here.
class BookModelAdmin(admin.ModelAdmin):
    list_display=['id','book_name','author_name','price','page','type_of_book']

admin.site.register(BookModel,BookModelAdmin)
