from django.urls import path
from blogs import views

urlpatterns = [
    path('create-blog/', views.createBlogView, name='create-blog'),
    path('list-blogs/', views.listBlogView, name='list-blogs'),
    path('<int:pk>/', views.detailBlogView, name='detail-blog'),
    path('update/<int:id>/', views.updateBlogView, name='update-blog'),
    path('delete/<int:pk>/', views.deletePostView, name='delete-blog'),
]