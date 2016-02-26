"""blog Views Configuration."""
from django.shortcuts import render


def post_list(request):
    """post_list View 설정."""
    return render(request, 'blog/post_list.html', {})
