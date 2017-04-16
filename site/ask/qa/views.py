from django.http import HttpResponse, HttpRequest, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.models import User as auth_models_User
from django.contrib.auth import authenticate, login
from django.views import generic
from django.core.exceptions import ObjectDoesNotExist
from .models import Question, Answer
from .forms import AskForm, AnswerForm, SignupForm


# Create your views here.
def test(request, *args, **kwargs):
    return HttpResponse("OK")


class IndexView(generic.ListView):
    model = Question
    template_name = "qa/base.html"
    context_object_name = "question_list"
    paginate_by = 10

    def get_queryset(self):
        return Question.objects.order_by("-added_at")


class PopularView(IndexView):
    def get_queryset(self):
        return Question.objects.order_by("-rating", "-added_at")


def _generate_test_user():
    try:
        stub_user = auth_models_User.objects.get(username="x")
    except ObjectDoesNotExist:
        stub_user = auth_models_User.objects.create_user(
            username="x", email="x@x.x", password="y")

    return stub_user


def question(request: HttpRequest, question_id: int):
    req_question = get_object_or_404(Question, id=question_id)
    related_answers = Answer.objects.all().order_by("added_at")

    if request.method == "POST":
        form = AnswerForm(request.POST)

        if form.is_valid():
            stub_user = _generate_test_user()
            # save new form
            new_answer = form.save(commit=False)
            new_answer.author = stub_user
            new_answer.save()

            return HttpResponseRedirect(
                reverse("qa:question", args=[question_id]))
    else:
        form = AnswerForm(initial={"question": question_id})

    return render(
        request,
        "qa/question.html",
        context={
            "question": req_question,
            "answers": related_answers.filter(question=req_question),
            "form": form
        })


def ask(request: HttpRequest):
    if request.method == "POST":
        form = AskForm(request.POST)

        if form.is_valid():
            stub_user = _generate_test_user()
            # save new form
            new_question = form.save(commit=False)
            new_question.author = stub_user
            new_question.save()
            # redirect to a new question page
            return HttpResponseRedirect(
                reverse("qa:question", args=[new_question.id]))
    else:
        # render empty form
        form = AskForm()

    return render(request, "qa/ask.html", {"form": form})


def signup(request: HttpRequest):
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(new_user.password)
            new_user.save()
            # get plain text password from request
            password = request.POST["password"]

            user = authenticate(
                request, username=new_user.username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)

                    return HttpResponseRedirect(reverse("qa:index"))
    else:
        form = SignupForm()

    return render(request, "qa/signup.html", {"form": form})
