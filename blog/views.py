from django.shortcuts import render, redirect
from .models import Blog
from .forms import PostForm, SearchForm

def home(request):
    form = SearchForm(request.GET or None)
    posts = Blog.objects.all()
    if form.is_valid():
        q = form.cleaned_data.get('q')
        if q:
            posts = posts.filter(title__icontains=q)
    return render(request, 'blog/home.html', {'posts': posts, 'form': form})

def create_post(request):
    page_title = 'Nuevo artículo'
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'blog/form.html', {'form': form, 'title': page_title})
