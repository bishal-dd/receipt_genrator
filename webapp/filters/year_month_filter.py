def year_month_filter(filter_item, year, month):
    if year and month:
        filter_item = filter_item.filter(date__year=year, date__month=month)
    elif year:
        filter_item = filter_item.filter(date__year=year)
    elif month:
        filter_item = filter_item.filter(date__month=month)

    return filter_item
