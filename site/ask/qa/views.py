from django.http import HttpResponse, HttpRequest
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Question


# Create your views here.
def test(request, *args, **kwargs):
    return HttpResponse("OK")


_QUESTION_ON_PAGE_LIMIT = 10
_FIRST_PAGE = 1


def page(request: HttpRequest):
    page_num = request.GET.get("page", _FIRST_PAGE)
    new_questions = Question.objects.new()
    paginator = Paginator(new_questions, _QUESTION_ON_PAGE_LIMIT)

    if page_num > paginator.num_pages:
        page_num = paginator.num_pages

    return render(
        request,
        "qa/base.html",
        context={"questions": paginator.page(page_num),
                 "page_num": page_num})
