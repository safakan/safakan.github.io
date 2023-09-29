from django.shortcuts import render
from django.views import View

from .models import BlogPost

# Create your views here.
class IndexView(View):
    def get(self, request):

        ## show blog posts
        posts = BlogPost.objects.all().order_by('-created_at')

        # only main index.html
        # return render(request, 'index.html')
        return render(request, 'index.html', {'posts': posts})