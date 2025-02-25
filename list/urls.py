from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path("login/", views.login_view, name="login"),
    path("signup/", views.signup_view, name="signup"),
    path("logout/", views.logout_view, name="logout"),
    path("add_todo/", views.add_todo, name="add_todo"),
    path("delete_todo/<int:todo_id>/", views.delete_todo, name="delete_todo"),
    path("about/", views.about, name="about")
]
