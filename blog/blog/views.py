from django.core.cache import cache
from django.shortcuts import render_to_response, get_object_or_404

from blog.blog.models import Blog, Category


def index(request):
    return render_to_response('index.html', {
        'categories': Category.objects.all(),
        'posts': Blog.objects.all()[:5]
    })


def view_post(request, slug):
    post = get_object_or_404(Blog, slug=slug)
    visits_count = cache.get(slug, 0) + 1
    cache.set(slug, visits_count)
    return render_to_response('view_post.html', {
        'post': post,
        'visits_count': visits_count,
    })


def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('view_category.html', {
        'category': category,
        'posts': Blog.objects.filter(category=category)[:5]
    })
