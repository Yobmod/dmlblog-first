from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib import messages
from .models import Post, Comment
from .forms import PostForm, CommentForm, TagIndexView, TagMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage
from django.contrib.auth.decorators import login_required

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date').reverse()
	paginator = Paginator(posts, 5)
	page_request_var = "post_page"
	page = request.GET.get(page_request_var)
	print(paginator.count)
	print(paginator.num_pages)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)#if not enough, give first page
	except(EmptyPage or InvalidPage):
		queryset = paginator.page(paginator.num_pages)#if too many, give last page
	context = {'posts':posts, 
						'page_request_var': page_request_var, 
						'obj_list':queryset,}
	return render(request, 'dmlblog/post_list.html', context)

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'dmlblog/post_detail.html', {'post': post})

@login_required
def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			messages.success(request, "New post created!")
			return redirect('blog:post_detail', pk=post.pk)
		else:
			messages.error(request, "New post failed!")
	else:
		form = PostForm()
	return render(request, 'dmlblog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST or None, request.FILES or None, instance=post)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.author = request.user
			instance.save()
			form.save_m2m()
			messages.success(request, "Post updated")
			return redirect('blog:post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'dmlblog/post_edit.html', {'form': form})


@login_required
def post_draft_list(request):
	posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
	return render(request, 'dmlblog/post_draft_list.html', {'posts': posts})

@login_required
def post_publish(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.publish()
	return redirect('blog:post_detail', pk=post.pk)

@login_required
def post_remove(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.delete()
	messages.success(request, "Post deleted")
	return redirect('blog:post_list')

def add_comment_to_post(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = post
			comment.save()
			return redirect('blog:post_detail', pk=post.pk)
	else:
		form = CommentForm()
	return render(request, 'dmlblog/add_comment_to_post.html', {'form': form})

@login_required
def comment_approve(request, pk):
	comment = get_object_or_404(Comment, pk=pk)
	comment.approve()
	return redirect('dmlblog.views.post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
	comment = get_object_or_404(Comment, pk=pk)
	post_pk = comment.post.pk
	comment.delete()
	return redirect('dmlblog.views.post_detail', pk=post_pk)

def tag_post(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return redirect('dmlblog.views.post_detail', pk=post.pk)
