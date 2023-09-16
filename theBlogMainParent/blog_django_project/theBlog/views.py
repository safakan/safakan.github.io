from django.shortcuts import render
from django.views import View

from .models import BlogPost

# Create your views here.
class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


# def blog_list(request):
#     posts = BlogPost.objects.filter(is_published=True).order_by('-created_at')
#     return render(request, 'blog_list.html', {'posts': posts})    