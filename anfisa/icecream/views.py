from django.http.response import HttpResponse
from django.shortcuts import render

from .models import icecream_db


def icecream_detail(request, pk):
    if pk > len(icecream_db):
        return HttpResponse('Нет такого мороженного...')
    name = icecream_db[pk]['name']
    description = icecream_db[pk]['description']
    context = {
        'name': name,
        'description': description,
    }
    return render(request, 'icecream/icecream-detail.html', context)
