from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateBlogForm, CreateComment
from django.contrib import messages
from .models import BlogPostsModel, CommentsModel
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.


def listBlogView(request):
    blogs = BlogPostsModel.objects.all()
    return render(request, 'blogs/listBlogs.html',{'blogs': blogs})

def detailBlogView(request, pk):
    try:
        blog = BlogPostsModel.objects.get(id = pk)
        comments = CommentsModel.objects.filter(post = blog)
        if request.method == 'POST':
            form = CreateComment(request.POST)
            if form.is_valid():
                form.save()
                return redirect('list-blogs')
        else:
            form = CreateComment()
        return render(request, 'blogs/detailBlog.html', {'blog': blog, 'form':form, 'comments': comments})
    except BlogPostsModel.DoesNotExist:
        return HttpResponse('No blog found')

@login_required
def createBlogView(request):
    if request.method == 'POST':
        createForm = CreateBlogForm(request.POST, request.FILES)
        if createForm.is_valid():
            createForm.save()
            messages.success(request, 'Blog has been created successfully')
            return redirect('create-blog')
        else:
            messages.error(request, 'Please correct the below errors')
    else:
        createForm = CreateBlogForm()

    return render(request, 'blogs/createBlog.html', {'form': createForm})


def updateBlogView(request, id):
    post = BlogPostsModel.objects.get(id = id)
    if request.method == 'POST':
        updateForm = CreateBlogForm(request.POST, request.FILES, instance = post) 
        if updateForm.is_valid():
            updateForm.save()
            messages.success(request, 'Blog has been updated successfully')
            return redirect('list-blogs')
        else:
            messages.error(request, 'Please correct the below errors')
    else:
        updateForm = CreateBlogForm(instance=post)
    
    return render(request, 'blogs/updateBlog.html', {'form': updateForm})

def deletePostView(request, pk):
    post = get_object_or_404(BlogPostsModel, id=pk)
    post.delete()
    return redirect('list-blogs')
