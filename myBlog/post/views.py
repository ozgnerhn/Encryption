from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect
from .models import Post
from .forms import PostForm
from django.contrib import messages


def post_index(request):
    posts = Post.objects.all()
    return render(request, 'post/index.html', {'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    context = {
        'post': post,
    }
    return render(request, 'post/detail.html', context)


def post_create(request):

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            messages.success(request, 'Başarılı Bir Şekilde Post Oluşturdunuz.', extra_tags='mesaj-basarili')
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        form = PostForm()

    context = {
        'form': form,
    }

    return render(request, 'post/form.html', context)


def post_update(request, id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        messages.success(request, 'Başarılı Bir Şekilde Postu Güncellediniz.')
        return HttpResponseRedirect(post.get_absolute_url())
    context = {
        'form': form,
    }
    return render(request, 'post/form.html', context)


def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('post:index')


