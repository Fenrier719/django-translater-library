from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from .forms import WordsForm
from .models import Words, FilesAdmin
from django.http import HttpResponse
import os

from django.views.static import serve


def general(request):
    error = ''
    word = []
    search_query = request.GET.get('search', '')
    if search_query:
        word = Words.objects.get(word__iexact=search_query)

    return render(request, 'main/general.html', context={'words': word})


def add_words(request):
    error = ''
    if request.method == 'POST':
        form = WordsForm(request.POST)
        if form.is_valid():
            form.save()

        else:
            error = 'Форма была неверной'

    form = WordsForm()
    data = {
        'form': form,
        'error': error
    }

    return render(request, 'main/add_words.html', data)


def show_books(request):
    search_query = request.GET.get('search', '')
    book = []
    if search_query:
        book = FilesAdmin.objects.filter(title__icontains=search_query)
    if search_query == '':
        book = FilesAdmin.objects.all()
    else:
        pass

    return render(request, 'main/library.html', context={'books': book})


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb')as fh:
            response = HttpResponse(
                fh.read(), content_type="application/adminupload")
            response['Content-Disposition'] = 'inline;filename=' + \
                os.path.basename(file_path)
            return response
    raise Http404
