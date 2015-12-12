from django.shortcuts import render
from .models import Post

def post_list(request):
	post = Post.objects.all().order_by("-pub_Date")
	return render(request,'blog/post_list.html',{'posts':post})

