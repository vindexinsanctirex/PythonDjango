from django.shortcuts import render
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.order_by("-updated_at")
    return render(request, "agenda/post_list.html", {'post_list': posts})