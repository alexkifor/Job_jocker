from django.db.models import Q
from employer.models import Vacancy
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def searchVacancies(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

 
    vacancies = Vacancy.objects.filter(status='ПУБЛИКАЦИЯ').distinct().filter(
        Q(profession__icontains=search_query) |
        Q(skills__icontains=search_query) |
        Q(description__icontains=search_query)
    )
    return vacancies, search_query


def paginateVacancies(request, vacancies, results):

    page = request.GET.get('page')
    paginator = Paginator(vacancies, results)

    try:
        vacancies = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        vacancies = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        vacancies = paginator.page(page)

    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, vacancies