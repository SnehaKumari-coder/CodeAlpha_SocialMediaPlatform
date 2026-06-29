from django.contrib import admin
from django.urls import path
from socialapp import views

urlpatterns = [
    path("admin/", admin.site.urls),   # <-- YE ADD KARNA HAI

    path("", views.login_page, name="login"),
    path("register/", views.register_page, name="register"),
    path("register_user/", views.register_user, name="register_user"),
    path("login_user/", views.login_user, name="login_user"),
    path("home/", views.home, name="home"),
    path("like/<int:post_id>/", views.like_post, name="like"),
    path("comment/<int:post_id>/", views.comment_post, name="comment"),
    path("profile/<str:username>/", views.profile, name="profile"),
    path("follow/<str:username>/", views.follow_user, name="follow"),
    path("logout/", views.logout_user, name="logout"),
]