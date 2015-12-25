from django.shortcuts import render , get_object_or_404
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect
from django.utils import timezone

def post_list(request):
	post = Post.objects.all().order_by("-pub_Date")
	return render(request,'blog/post_list.html',{'posts':post})

def post_detail(request,pk):
	post = get_object_or_404(Post,pk=pk)
	return render(request,'blog/post_detail.html',{'post':post})

	
def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.pub_Date = timezone.now()
			post.save()
			return redirect('post_detail',pk=post.pk)

	else:
		form = PostForm()
		return render(request,'blog/post_new.html',{'form':form})


def post_edit(request,pk):
	post = get_object_or_404(Post,pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST,instance = post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.pub_Date = timezone.now()
			post.save()
			return redirect('post_detail',pk=post.pk)

	else:
		form = PostForm(instance = post)
		return render(request,'blog/post_new.html',{'form':form})
