from django.shortcuts import render

import calendar

from django.http import HttpResponse
from django.utils import timezone


def index(request):
    current_year = timezone.now().year
    calendar_html = calendar.HTMLCalendar().formatyear(current_year)

    return render(request, 'qa/index.html', {
        'current_year': current_year,
        'calendar_html': calendar_html,
    })
