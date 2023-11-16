from django.shortcuts import render, redirect
from .models import Articles
from .forms import PrepositionalNewsForm


def news_home(request):
    news = Articles.objects.all()

    return render(request, 'news/news.html', {'news': news,
                                              'title': 'Новости'}
                  )


def news_prepNews(request):
    error = ''
    if request.method == "POST":
        form = PrepositionalNewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news')
        else:
            error = 'Форма заполнена неверно'
    form = PrepositionalNewsForm()
    return render(request, 'news/prepositionalNews.html', {'form': form,
                                                           'error': error,
                                                           'title': 'Предложить новость'}
                  )
