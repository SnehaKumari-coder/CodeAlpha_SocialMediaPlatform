from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Post, Comment, Follow


# LOGIN PAGE
def login_page(request):
    return render(request, "login.html")


# REGISTER PAGE
def register_page(request):
    return render(request, "register.html")


# REGISTER USER
def register_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {"error": "Username exists"})

        User.objects.create_user(username=username, password=password)
        return redirect("/")

    return redirect("/register/")


# LOGIN USER
def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect("/home/")

        return render(request, "login.html", {"error": "Wrong credentials"})

    return redirect("/")


# HOME
def home(request):
    if not request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        content = request.POST["content"]
        Post.objects.create(user=request.user, content=content)

    posts = Post.objects.all().order_by("-id")
    comments = Comment.objects.all()

    return render(request, "home.html", {
        "posts": posts,
        "comments": comments
    })


# LIKE POST
def like_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.likes += 1
    post.save()

    return redirect("/home/")


# COMMENT POST
def comment_post(request, post_id):
    if request.method == "POST":
        post = Post.objects.get(id=post_id)
        text = request.POST["comment"]

        Comment.objects.create(
            post=post,
            user=request.user,
            text=text
        )

    return redirect("/home/")


# PROFILE
def profile(request, username):
    user = User.objects.get(username=username)

    posts = Post.objects.filter(user=user).count()
    followers = Follow.objects.filter(following=user).count()
    following = Follow.objects.filter(follower=user).count()

    return render(request, "profile.html", {
        "user_profile": user,
        "posts": posts,
        "followers": followers,
        "following": following
    })


# FOLLOW USER
def follow_user(request, username):
    target = User.objects.get(username=username)

    if request.user != target:
        Follow.objects.get_or_create(
            follower=request.user,
            following=target
        )

    return redirect(f"/profile/{username}/")


# LOGOUT
def logout_user(request):
    logout(request)
    return redirect("/")