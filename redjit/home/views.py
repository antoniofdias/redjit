from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm, PostForm, CommentForm
from .models import Post

def frontpage(request):
  posts = Post.objects.all()

  if request.method == 'POST':
    form = PostForm(request.POST)

    if form.is_valid():
      post = form.save(commit=False)
      post.username = request.user.username
      post.save()

      return redirect('frontpage')

  context = {
    "posts": posts
  }

  return render(request, 'home/frontpage.html', context)

def auth_login(request):
  if request.user.is_authenticated:
    return redirect('frontpage')

  else:
    if request.method == "POST":
      username = request.POST.get('username')
      password = request.POST.get('password')

      user = authenticate(request, username=username, password=password)

      if user is not None:
        login(request, user)
        return redirect('frontpage')
      else:
        messages.info(request, 'Usuário e/ou senha incorretos.')
        return render(request, 'home/login.html')

    return render(request, 'home/login.html')

def auth_logout(request):
  logout(request)
  return redirect('auth_login')

def register(request):
  if request.user.is_authenticated:
    return redirect('frontpage')

  else:
    form = CreateUserForm()

    if request.method =='POST':
      form = CreateUserForm(request.POST)
      if form.is_valid():
        form.save()
        messages.success(request, 'Conta criada! Faça o login acima.')

        return redirect('auth_login')

    context = {
      "form": form
    }

    return render(request, 'home/register.html', context)

@login_required(login_url='auth_login')
def post_detail(request, slug):
  post = Post.objects.get(slug=slug)

  if request.method == 'POST':
    form = CommentForm(request.POST)

    if form.is_valid():
      comment = form.save(commit=False)
      comment.post = post
      comment.username = request.user.username
      comment.save()

      return redirect('post_detail', slug=post.slug)
  else:
    form = CommentForm()

  context = {
    "post": post,
    "form": form
  }

  return render(request, 'home/post_detail.html', context)

# Crie a view "new_post", que renderiza o template'home/create_post.html',
# que só pode ser acessada caso o usuário esteja logado e
# recebe um formulário de post em seu contexto.

def new_post(request):
  return
