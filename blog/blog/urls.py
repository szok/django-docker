from django.conf.urls import patterns, url

urlpatterns = [
    url(r'^$', 'blog.blog.views.index'),
    url(
        r'^view/(?P<slug>[^\.]+).html',
        'blog.blog.views.view_post',
        name='view_blog_post'
    ),
    url(
        r'^category/(?P<slug>[^\.]+).html',
        'blog.blog.views.view_category',
        name='view_blog_category'
    ),
]
