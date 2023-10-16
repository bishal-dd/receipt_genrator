from django.core.paginator import Paginator


def pagination(request, paginated_item, items_per_page):
    paginator = Paginator(paginated_item, items_per_page)
    page = request.GET.get('page')
    paginated_item = paginator.get_page(page)

    return paginated_item

