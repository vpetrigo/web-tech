from django.http import HttpResponse, HttpRequest, Http404
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Question


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
