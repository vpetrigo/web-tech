from django.conf.urls import url
from . import views

app_name = "qa"

urlpatterns = [
    url("^$", views.main_page, name="index"),
    url("^login/$", views.test, name="login"),
    url("^signup/$", views.test, name="signup"),
    url("^question/(?P<question_id>\d+)/$", views.question, name="question"),
    url("^ask/.*$", views.test, name="ask"),
    url("^popular/$", views.popular_page, name="popular"),
    url("^new/$", views.test, name="new"),
]
