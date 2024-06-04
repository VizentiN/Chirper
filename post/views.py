from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from post.models import Post

def home(request):
    if request.user.is_authenticated:
        return redirect('posts') 
    
    return render(request, 'index.html')

def posts(request):
    if request.user.is_authenticated:
        posts = Post.objects.all().order_by('-created_at')
        return render(request, 'posts.html', {'posts': posts})
    else:
        return render(request, 'index.html')

@login_required
def create_post(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        post = Post(user=request.user, content=content)
        post.save()
        return redirect('posts')
    else:
        # Renderizar um formulário para criar um novo post, pode ser a própria página de posts ou uma modal
        return render(request, 'create_post.html')