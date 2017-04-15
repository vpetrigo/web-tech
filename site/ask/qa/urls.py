from django.conf.urls import url
from . import views

app_name = "qa"

urlpatterns = [
    url("^$", views.IndexView.as_view(), name="index"),
    url("^login/$", views.test, name="login"),
    url("^signup/$", views.test, name="signup"),
    url("^question/(?P<question_id>\d+)/$", views.question, name="question"),
    url("^ask/$", views.ask, name="ask"),
    url("^popular/$", views.PopularView.as_view(), name="popular"),
    url("^new/$", views.test, name="new"),
]
