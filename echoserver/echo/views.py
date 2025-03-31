from django.shortcuts import render
from echo.models import Book
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.db import connection
from django.core.paginator import Paginator
from django.db.utils import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import CustomUserCreationForm
import math


def home_page_view(request):
    books = list(Book.objects.all().order_by("id"))
    is_active = False

    current_user = request.user
    if request.user.id is not None:
        is_active = True

    header = "Список книг"
    data = {"header": header, "books": books, "limit": 0, "page": 1,
            "pages_list": [], "current_user": current_user, "is_active": is_active}
    return render(request, "index.html", context=data)


def home_page_view_with_params(request, limit=0, page=1):
    books = list(Book.objects.all().order_by("id"))

    is_active = False

    current_user = request.user
    if request.user.id is not None:
        is_active = True

    if limit != 0:
        total_pages = math.ceil(len(books) / limit)
        if 1 <= page <= total_pages and total_pages > 1:
            p = Paginator(books, limit)
            pages_list = [i for i in range(1, total_pages + 1)]
            header = "Список книг"
            data = {"header": header, "books": p.page(page).object_list, "limit": limit, "page": page,
                    "pages_list": pages_list, "current_user": current_user, "is_active": is_active}

            return render(request, "index.html", context=data)
        else:
            return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/")


def page_add_book(request):
    if request.user is not None:
        return render(request, "add.html")


def submit_add_book(request):
    try:
        if request.method == "POST" and request.user is not None:
            book = Book()
            book.name = request.POST.get("book_name")
            book.author = request.POST.get("book_author")
            book.price = request.POST.get("book_price")
            book.genre = request.POST.get("book_genre")
            book.public_date = request.POST.get("book_public_date")
            book.publisher = request.POST.get("book_publisher")
            book.save()
        return HttpResponseRedirect("/")
    except IntegrityError:
        return HttpResponse("Введите корректные значения...")
    except ValueError:
        return HttpResponse("Введите корректные значения...")


def page_edit_book(request, id):
    # даже не зарегестрирован
    if request.user is None:
        return HttpResponseRedirect("/")

    try:
        book = Book.objects.get(id=id)

        if request.method == "POST":
            book.name = request.POST.get("book_name")
            book.author = request.POST.get("book_author")
            book.price = request.POST.get("book_price")
            book.genre = request.POST.get("book_genre")
            book.public_date = request.POST.get("book_public_date")
            book.publisher = request.POST.get("book_publisher")
            book.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"book": book})

    except Book.DoesNotExist:
        return HttpResponseNotFound("<h2>Model Book has not found</h2>")


def page_delete_book(request, id):
    if request.user is None:
        return HttpResponseRedirect("/")

    try:
        book = Book.objects.get(id=id)
        book.delete()
        return HttpResponseRedirect("/")

    except Book.DoesNotExist:
        return HttpResponseNotFound("<h2>Model Book has not found</h2>")



def page_signup(request):
    form = CustomUserCreationForm()
    return render(request, "signup.html", {"form": form})


def submit_signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    return HttpResponseRedirect("/")


def page_signin(request):
    return render(request, "signin.html")


def submit_signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
    return HttpResponseRedirect("/")


def page_signout(request):
    user = logout(request)
    return HttpResponseRedirect("/")


