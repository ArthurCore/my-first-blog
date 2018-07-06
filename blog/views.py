from django.shortcuts import render
from .models import Post


#실습1
def post_list(request):
    return render(request, 'blog/post_list.html', {})

#실습2
def test(request):
    post_list = Post.objects.all()
    return render(request, 'blog/test.html', {
        'post_list' : post_list,
    })

def post_detail(request, pk):
    post = Post.objects.get(pk=pk) # 페이지 찾지 못하면 Post.DeseNotExist 500error
    return render(request, 'blog/post_detail.html', {
        'post' : post,
    })
