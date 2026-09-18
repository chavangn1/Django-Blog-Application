from django.urls import path
from . import views


urlpatterns = [

    # Blog
    path('create-blog/',views.createBlogView,name='create-blog'),
    path('list-blogs/',views.listBlogView,name='list-blogs'),
    path('<int:pk>/',views.detailBlogView,name='detail-blog'),
    path('update/<int:id>/',views.updateBlogView,name='update-blog'),
    path('delete/<int:pk>/',views.deletePostView,name='delete-blog'),
    path('search-blogs/', views.searchBlogsView, name = 'search-blogs'),

    # Comments
    path('edit-comments/<int:pk>/',views.editCommentView,name='edit-comments'),
    path('delete-comments/<int:pk>/',views.deleteCommentView,name='delete-comments'),


]
