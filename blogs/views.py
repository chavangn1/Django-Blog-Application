from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from .forms import (CreateBlogForm, CreateCommentForm, EditCommentForm)
from .models import (BlogPostsModel, CommentsModel)
from django.db.models import Case, When, Value, IntegerField
from django.core.paginator import Paginator


def listBlogView(request):
    blogs = BlogPostsModel.objects.all().order_by('-created_at')
    return render(request, 'blogs/listBlogs.html', {'blogs': blogs})


def detailBlogView(request, pk):

    blog = get_object_or_404(BlogPostsModel, id=pk)
    comments = CommentsModel.objects.filter(post=blog).order_by('-created_at')

    if request.user.is_authenticated:
        comments = CommentsModel.objects.filter(post=blog).annotate(priority=Case(When(author=request.user,then=Value(0)),
                default=Value(1),output_field=IntegerField())).order_by('priority','-created_at')

    if request.method == 'POST':

        # User must be logged in
        if not request.user.is_authenticated:

            return redirect(f'/login/?next={request.path}')

        # Check if this user already commented
        already_commented = CommentsModel.objects.filter(author=request.user,post=blog).exists()

        if already_commented:

            messages.error(request,'You have already commented on this post.')

            return redirect('detail-blog',pk=blog.id)


        # Create comment form
        form = CreateCommentForm(request.POST)

        if form.is_valid():

            comment = form.save(commit=False)

            # Set these ourselves
            comment.author = request.user
            comment.post = blog

            comment.save()

            messages.success(request,'Comment added successfully!')

            return redirect('detail-blog',pk=blog.id)

    else:

        form = CreateCommentForm()

    return render(request,'blogs/detailBlog.html',{'blog': blog,'comments': comments,'form': form,})


@login_required
def editCommentView(request, pk):

    comment = get_object_or_404(CommentsModel, id=pk)

    # Only comment owner can edit
    if comment.author != request.user:

        raise PermissionDenied('You are not allowed to edit this comment.')

    if request.method == 'POST':

        form = EditCommentForm(request.POST,instance=comment)

        if form.is_valid():

            form.save()

            messages.success(request,'Comment updated successfully!')

    return redirect('detail-blog',pk=comment.post.id)



@login_required
@require_POST
def deleteCommentView(request, pk):

    comment = get_object_or_404(CommentsModel,id=pk)

    # Only comment owner can delete
    if comment.author != request.user:

        raise PermissionDenied('You are not allowed to delete this comment.')

    post_id = comment.post.id

    comment.delete()

    messages.success(request,'Comment deleted successfully!')

    return redirect('detail-blog',pk=post_id)


@login_required
def createBlogView(request):

    if request.method == 'POST':

        form = CreateBlogForm(request.POST,request.FILES)

        if form.is_valid():

            user = form.save(commit=False)

            user.author = request.user

            user.save()

            messages.success(request,'Blog has been created successfully.')

            return redirect('list-blogs')

        messages.error(request,'Please correct the below errors.')

    else:

        form = CreateBlogForm()

    return render(request,'blogs/createBlog.html',{'form': form})


@login_required
def updateBlogView(request, id):

    post = get_object_or_404(BlogPostsModel,id=id)

    if post.author != request.user:

        raise PermissionDenied('You are not allowed to edit this post.')

    if request.method == 'POST':

        form = CreateBlogForm(request.POST,request.FILES,instance=post)

        if form.is_valid():

            form.save()

            messages.success(request,'Blog has been updated successfully.')

            return redirect('detail-blog', pk=post.id)

    else:

        form = CreateBlogForm(instance=post)

    return render(request,'blogs/updateBlog.html',{'form': form})


@login_required
@require_POST
def deletePostView(request, pk):

    post = get_object_or_404(BlogPostsModel,id=pk)

    if post.author != request.user:
    
        raise PermissionDenied('You are not allowed to edit this post.')

    post.delete()

    messages.success(request,'Blog deleted successfully.')

    return redirect('list-blogs')


def searchBlogsView(request):
    search = request.GET.get('search_blogs')
    blogs = BlogPostsModel.objects.filter(title__icontains = search)
    return render(request, 'accounts/dashboard.html', {'blogs': blogs})