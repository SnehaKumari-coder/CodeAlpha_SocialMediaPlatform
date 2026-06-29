from django.urls import path
from . import views


urlpatterns = [

    # Login page
    path("", views.login_page, name="login"),

    # Register page
    path("register/", views.register_page, name="register"),

    # Register user
    path("register_user/", views.register_user, name="register_user"),

    # Login user
    path("login_user/", views.login_user, name="login_user"),

    # Home
    path("home/", views.home, name="home"),

    # Like post
    path("like/<int:post_id>/", views.like_post, name="like"),

    # Comment post
    path("comment/<int:post_id>/", views.comment_post, name="comment"),

    # Profile page
    path("profile/<str:username>/", views.profile, name="profile"),

    # Follow user
    path("follow/<str:username>/", views.follow_user, name="follow"),

    # Logout
    path("logout/", views.logout_user, name="logout"),
]