from django.shortcuts import render,redirect
from django.http import HttpResponse
from app1.models import BookModel
from app1.manager import AppManager
from app1.forms import registerform
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth import logout



@login_required()
def home(request):
    content={}
    content['data']=BookModel.obj.all()
    return render(request,'app1/home.html',content)

def register(request):
    if request.method=='POST':
        data=registerform(request.POST)
        if data.is_valid():
            data.save()
            messages.success(request,' Registered Sucessfully !!!')
            return redirect('/')
        else:
            messages.error(request,' ERROR , FILL CORRECT DETAILS !!!')
            return redirect('/register/')
    else :
        f=registerform()
        content={'form':f}
        return render(request,'app1/register.html', content)

# Create your views here.
@permission_required('app1.add_bookmodel' ,login_url="/errorshow/")
def add(request):
    if not request.user.is_authenticated:
        return redirect('/')
    elif (request.method=='POST'):
        if(request.method == 'POST'):
            bookname__ = request.POST['bname'] #this banme is the name attribute of input tag in add.html
            authorname__ = request.POST['aname']
            price__ = request.POST['price']
            page__ = request.POST['pages']
            booktype__ = request.POST['booktype']
            # print(bookname__)
            # print(authorname__)
            # print(price__)
            # print(page__)
            # print(booktype__)
        
            #creating query to insert sql data into Table
            #model_class.obj.insert(columnname = value)
            insert_data=BookModel.obj.create(book_name=bookname__ , author_name=authorname__ ,price=price__,page=page__ ,type_of_book=booktype__)
            #executing  the query
            insert_data.save()
            return redirect("/")
    else:
        return render(request,'app1/add.html')
        
        
def errorshow(request):
    return render(request,'app1/errorshow.html')

@permission_required('app1.delete_bookmodel' ,login_url="/errorshow/")
def delete(request,tid):
    if not request.user.is_authenticated:
        return redirect('/')
    else:
        record_to_be_deleted=BookModel.obj.filter(id=tid)
        record_to_be_deleted.delete()
        return redirect("/")
    
@permission_required('app1.change_bookmodel' ,login_url="/errorshow/")
def update(request,tid):
    if not request.user.is_authenticated:
        return redirect('/')
    elif (request.method == 'POST'):
        if(request.method=="POST"):
            bookname__ = request.POST['bname']  #this banme is the name attribute of input tag in html file
            authorname__ = request.POST['aname']
            price__ = request.POST['price']
            page__ = request.POST['pages']
            booktype__ = request.POST['booktype']
            record_to_be_update=BookModel.obj.filter(id=tid)
            record_to_be_update.update(book_name=bookname__ , author_name=authorname__ ,price=price__,page=page__ ,type_of_book=booktype__)
            return redirect("/")
    else:
            content={}
            content['data']=BookModel.obj.get(id=tid)
            return render(request,'app1/update.html',content)
    
def htol(request):
    if not request.user.is_authenticated:
        return redirect('/')
    content={}
    content['data']=BookModel.obj.all_price_in_descending_order()
    return render(request,'app1/home.html',content)
    
    
def ltoh(request):
    if not request.user.is_authenticated:
        return redirect('/')
    content={}
    content['data']=BookModel.obj.all_price_in_ascending_order()
    return render(request,'app1/home.html',content)
        
def catfilter(request,cat):
    if not request.user.is_authenticated:
        return redirect('/')
    content={}
    content['data']=BookModel.obj.filter(type_of_book=cat)
    return render(request,'app1/home.html',content)
    
def bookname_ATOZ(request):
    if not request.user.is_authenticated:
        return redirect('/')
    content={}
    content['data']=BookModel.obj.sort_by_bookname_ATOZ()
    return render(request,'app1/home.html',content)

def bookname_ZTOA(request):
    if not request.user.is_authenticated:
        return redirect('/')
    content={}
    content['data']=BookModel.obj.sort_by_bookname_ZTOA()
    return render(request,'app1/home.html',content)

def authorname_ATOZ(request):
    if not request.user.is_authenticated:
        return redirect('/')
    content={}
    content['data']=BookModel.obj.sort_by_authorname_ATOZ()
    return render(request,'app1/home.html',content)


def authorname_ZTOA(request):
    if not request.user.is_authenticated:
        return redirect('/')
    content={}
    content['data']=BookModel.obj.sort_by_authorname_ZTOA()
    return render(request,'app1/home.html',content)

def id_htol(request):
    if not request.user.is_authenticated:
        return redirect('/')
    content={}
    content['data']=BookModel.obj.sort_by_id_htol()
    return render(request,'app1/home.html',content)

def id_ltoh(request):
    if not request.user.is_authenticated:
        return redirect('/')
    content={}
    content['data']=BookModel.obj.sort_by_id_ltoh()
    return render(request,'app1/home.html',content)
    
    


    