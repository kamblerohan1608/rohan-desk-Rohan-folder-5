from django.urls import path
from . import views



urlpatterns = [
    path('',views.home.as_view(),name='home'),
    path('register/',views.register.as_view(),name='register'),
    path('dashboard/',views.dashboard.as_view(),name='dashboard'),
    path('signout/',views.signout.as_view(),name='signout'),
    path('add_blog/',views.add_blog.as_view(),name='add_blog'),
    path('all_blogs/',views.all_blogs.as_view(),name='all_blogs'),
    path('delete_blog/<int:pk>',views.delete_blog.as_view(),name='delete_blog'),
    path('edit_blog/<int:pk>',views.edit_blog.as_view(),name='edit_blog'),
    
]