from django.http import HttpResponse, HttpRequest, Http404, HttpResponseRedirect
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Question, Answer
from .forms import AskForm, AnswerForm


# Create your views here.
def test(request, *args, **kwargs):
    return HttpResponse("OK")


_QUESTION_ON_PAGE_LIMIT = 10
_FIRST_PAGE = 1


def _paginate_content(request: HttpRequest, content_getter):
    try:
        page_num = int(request.GET.get("page", _FIRST_PAGE))
    except ValueError:
        page_num = _FIRST_PAGE

    content = content_getter()
    paginator = Paginator(content, _QUESTION_ON_PAGE_LIMIT)

    if page_num < 1:
        page_num = _FIRST_PAGE
    elif page_num > paginator.num_pages:
        page_num = paginator.num_pages

    return paginator, page_num


def main_page(request: HttpRequest):
    paginator, page_num = _paginate_content(request, Question.objects.new)

    return render(
        request,
        "qa/base.html",
        context={"questions": paginator.page(page_num),
                 "page_num": page_num})


def popular_page(request: HttpRequest):
    paginator, page_num = _paginate_content(request, Question.objects.popular)

    return render(
        request,
        "qa/base.html",
        context={"questions": paginator.page(page_num),
                 "page_num": page_num})


def question(request: HttpRequest, question_id: int):
    req_question = get_object_or_404(Question, id=question_id)
    related_answers = Answer.objects.all()

    return render(
        request,
        "qa/question.html",
        context={
            "question": req_question,
            "answers": related_answers.filter(question=req_question)
        })


def ask(request: HttpRequest):
    if request.method == "POST":
        form = AskForm(request.POST)

        if form.is_valid():
            # save new form
            new_question = form.save()
            # redirect to a new question page
            return HttpResponseRedirect(
                reverse("qa:question"), args=new_question.id)
    else:
        # render empty form
        form = AskForm()

        return render(request, "qa/ask.html", {"form": form})
