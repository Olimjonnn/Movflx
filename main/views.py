from django.shortcuts import render
from main.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def Index(request):
    blogmain = BlogMain.objects.last()
    main = Main.objects.last()
    upcmovies = UpcMovies.objects.all()
    ind = Ind.objects.all()
    a = {
        'main':main,
        'blogmain':blogmain,
        'upcmovies':upcmovies,
        'ind':ind,
    }
    return render(request, "index.html", a)



def PagenatorPage(List, num, request):
    paginator = Paginator(List, num)
    pages = request.GET.get("page")
    try:
        list = paginator.page(pages)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)
    return list




def Contact(request):
    return render(request, "contact.html")



def Blog(request):
    blogmain = BlogMain.objects.last()
    blogs = Blogs.objects.all().order_by("-id")[0:3]
    c = {
        'blogmain':blogmain,
        'blogs':PagenatorPage(blogs, 1, request),
    }
    return render(request, "blog.html",c)



def Movie(request):
    return render(request, "movie.html")



def MovieDetails(request, pk):
    movie = Ind.objects.get(id=pk)
    a = {
        'movie':movie
    }
    return render(request, "movie-details.html", a)



def BlogDetails(request, pk):
    blogs = Blogs.objects.get(id=pk)
    a = {
        'blogs':blogs
    }
    return render(request, "blog-details.html", a)
