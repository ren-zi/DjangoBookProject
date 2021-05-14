from django.shortcuts import render,redirect
from app01 import models
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
# Create your views here.
def add_publisher(request):
    if request.method == 'POST':

        publish_name = request.POST.get('name')

        publish_address = request.POST.get('address')

        models.Publisher.objects.create(name=publish_name, address=publish_address)

        return redirect('/app01/publisher_list')

    return render(request, 'add_publisher.html')


def publisher_list(request):
    if request.method == "POST":
        name = request.POST.get('name')
        publisher_obj = models.Publisher.objects.get(name=name)
        return render(request,'publisher_search.html',{'publisher_obj':publisher_obj})

    publisher_list = models.Publisher.objects.all()
    return render(request,'publisher_list.html',{'publisher_obj_list':publisher_list})

def delete_publisher(request):
    if request.method == 'POST':
        id = request.POST.get('id')

        models.Publisher.objects.get(id=id).delete()

        return redirect('/app01/publisher_list/')
    else:
        id=request.GET.get('id')
        publisher_obj = models.Publisher.objects.get(id=id)

        return render(request,'delete_publisher.html',{'publisher_obj':publisher_obj})

def edit_publisher(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        address = request.POST.get('address')
        publisher_obj = models.Publisher.objects.get(id=id)

        #修改
        publisher_obj.name = name
        publisher_obj.address = address
        publisher_obj.save()
        return redirect('/app01/publisher_list/')
    else:
        id = request.GET.get('id')
        publisher_obj=models.Publisher.objects.get(id=id)
        publisher_obj_list=models.Publisher.objects.all()
        return render(request,'edit_publisher.html',{'publisher_obj':publisher_obj,'publisher_obj_list':publisher_obj_list})

def book_list(request):
    if request.method =='GET':
        book_obj = models.Book.objects.all()
        paginator = Paginator(book_obj, 10)  # 每页显示8条数据
        #print(paginator.count)  # 总数据条数
        #print(paginator.num_pages)  # 总页数
        #print(paginator.page_range)  # 页数范围

        current_page_num = int(request.GET.get('page', 1))  # 通过a标签的GET方式请求，默认显示第一页
        book_objs = paginator.page(current_page_num)  # 获取当前页面的数据
        if book_objs.has_previous():  # 当前页面是否有前一页
            print(book_objs.previous_page_number())  # 当前页面的前一页页码
        if book_objs.has_next():  # 当前页面是否有后一页
            print(book_objs.next_page_number())  # 当前页面的后一页页码

        page_range = paginator.page_range
        if paginator.num_pages > 5:  # 页码只显示5页，总页数小于5页时，直接全部显示
            if current_page_num < 3:
                page_range = range(1, 6)
            elif current_page_num + 2 > paginator.num_pages:
                page_range = range(paginator.num_pages - 5, paginator.num_pages + 1)
            else:
                page_range = range(current_page_num - 2, current_page_num + 3)

        return render(request, 'book_list.html',
                      {'book_objs': book_objs, 'page_range': page_range, 'current_page_num': current_page_num})
    elif request.method == 'POST':
        book_name = request.POST.get('book_name')
        book_obj_list = models.Book.objects.filter(book_name=book_name)
        return render(request,'book_search.html',{'book_obj_list':book_obj_list})






def add_book(request):
    if request.method == 'POST':
        book_name = request.POST.get('book_name')
        author = request.POST.get('author')
        publisher = request.POST.get('publisher')
        book_put_on = request.POST.get('book_put_on')
        price = request.POST.get('price')
        score = request.POST.get('score')
        comment_num = request.POST.get('comment_num')
        models.Book.objects.create(book_name=book_name, author=author, publisher=publisher,book_put_on=book_put_on,
                                   price=price,score=score,comment_num=comment_num)
        return redirect('/app01/book_list/')
    return render(request, 'add_book.html')

def edit_book(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        book_name = request.POST.get('book_name')
        author = request.POST.get('author')
        publisher = request.POST.get('publisher')
        book_put_on = request.POST.get('book_put_on')
        price = request.POST.get('price')
        score = request.POST.get('score')
        comment_num = request.POST.get('comment_num')
        #修改
        book_obj = models.Book.objects.get(id=id)
        book_obj.book_name = book_name
        book_obj.author = author
        book_obj.publisher = publisher
        book_obj.book_put_on = book_put_on
        book_obj.price = price
        book_obj.score = score
        book_obj.comment_num = comment_num
        book_obj.save()
        return redirect('/app01/book_list/')

    else:
        id = request.GET.get('id')
        book_obj = models.Book.objects.get(id=id)
        return render(request,'edit_book.html',{'book_obj':book_obj})

def delete_book(request):
    if request.method == 'POST':
        id = request.POST.get('id')

        models.Book.objects.get(id=id).delete()

        return redirect('/app01/book_list/')
    else:
        id = request.GET.get('id')
        book_obj = models.Book.objects.get(id=id)

        return render(request, 'delete_book.html', {'book_obj': book_obj})

def author_list(request):
    if request.method == 'POST':
        aname = request.POST.get('name')
        author_obj_list = models.Author.objects.get(name=aname)
        return render(request,'author_search.html',{'author_obj':author_obj_list})
    author_obj_list = models.Author.objects.all()
    return render(request,'author_list.html',{'author_obj_list':author_obj_list})


def add_author(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        models.Author.objects.create(name=name,address=address)

        return redirect('/app01/author_list/')
    return render(request,'add_author.html')


def delete_author(request):
    if request.method == 'POST':
        id = request.POST.get('id')

        models.Author.objects.get(id=id).delete()

        return redirect('/app01/author_list/')
    else:
        id = request.GET.get('id')
        author_obj = models.Author.objects.get(id=id)

        return render(request, 'delete_author.html', {'author_obj': author_obj})

def edit_author(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        address = request.POST.get('address')

        #修改
        author_obj = models.Author.objects.get(id=id)
        author_obj.name = name
        author_obj.address = address

        author_obj.save()
        return redirect('/app01/author_list/')

    else:
        id = request.GET.get('id')
        author_obj = models.Author.objects.get(id=id)
        return render(request,'edit_author.html',{'author_obj':author_obj})

def login(request):
    if request.method == "POST":
        name = request.POST.get('name')
        password = request.POST.get('password')
        user = models.User.objects.filter(name=name, password=password)
        if user:
            # 比较成功
            return redirect('/app01/book_list/')
        else:
            # 比较失败 重新输入
            return redirect('/login/')

    return render(request,'login.html')









def regist(request):
    if request.method == "POST":
        name = request.POST.get('name')
        password = request.POST.get('password')
        models.User.objects.create(name=name, password=password)

        return redirect('/login/')

    return render(request,'regist.html')

def views(request):
    return render(request,'gdp.html')
# def book_search(request):
#     qbname = request.GET.get('qbname')
 #    book_obj = models.Book.objects.get(name=qbname)

 #    return render(request,'book_search.html',{'book_obj':book_obj})