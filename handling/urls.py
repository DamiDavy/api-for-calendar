from django.urls import path

from . import views

urlpatterns = [
    path('is_logged_in', views.is_logged_in, name="is_logged_in"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("registration", views.register, name="register"),

    path("", views.hi, name="hi"),
    path("todos", views.todos, name="todos"),
    path("todo", views.add_delete_todo, name="add_delete_todo"),

    # # API Routes
    # path("emails", views.compose, name="compose"),
    # path("emails/<int:email_id>", views.email, name="email"),
    # path("emails/<str:mailbox>", views.mailbox, name="mailbox"),
]
