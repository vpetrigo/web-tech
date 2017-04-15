from django.http import HttpResponse, HttpRequest, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.models import User as auth_models_User
from django.views import generic
from .models import Question, Answer
from .forms import AskForm, AnswerForm


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


def question(request: HttpRequest, question_id: int):
    req_question = get_object_or_404(Question, id=question_id)
    related_answers = Answer.objects.all().order_by("added_at")

    if request.method == "POST":
        form = AnswerForm(request.POST)

        if form.is_valid():
            stub_user, created = auth_models_User.objects.get_or_create(
                username="x", password="y")
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
            stub_user, created = auth_models_User.objects.get_or_create(
                username="x", password="y")
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
