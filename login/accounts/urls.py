from django.urls import  path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path('',views.indexView,name="login"),
    path('suggestions/',views.suggestions_view,name="suggestions"),
    path('editprofile/',views.edit_view,name="edit"),
    path('viewpost/',views.post_view,name="viewpost"),
    path('like/',views.like_post,name="like-post"),
    path('addpost/',views.addpostview,name="addpost"),
    path('home/',views.dashboardView,name="home"),
    path('login/',LoginView.as_view(),name="login_url"),
    path('register/',views.registerView,name="register_url"),
    path('logout/',LogoutView.as_view(next_page="login"),name="logout"),
]








