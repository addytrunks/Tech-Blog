
from django.urls import path
from blog import views
from .views import (HomeView,ArticleDetailView,AddPostView,
                    UpdatePostView,DeletePostView,
                    CategoryListView,
                    )

app_name = 'blog'

#create your paths here
urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),

    path('details/<int:pk>',views.ArticleDetailView.as_view(),name='detail'),
    path('addpost/',views.AddPostView.as_view(),name='add_post'),
    path('update/<int:pk>',views.UpdatePostView.as_view(),name='update_post'),
    path('delete/<int:pk>',views.DeletePostView.as_view(),name='delete_post'),

    path('category/<str:cats>',views.CategoryView,name='category'),
    path('category_list',views.CategoryListView.as_view(),name='category_list'),

    path('about',views.about,name='about'),
    path('search/',views.search,name='search'),


    path('like/<int:pk>',views.LikeViews,name="like_post"),
    path('profile',views.Profile,name='profile'),

]
