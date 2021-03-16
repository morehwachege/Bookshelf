from django.shortcuts import render
from book_function import scrapper


def home(request):
    link = 'https://manybooks.net/search-book?field_genre[30]=30'
    book_list = scrapper(link)
    # editors picks section below
    picks = 'https://manybooks.net/search-book?field_genre[38]=38'
    picks_list = scrapper(picks)
    complete_link = 'http://manybooks.net'
    book_number = len(book_list)
    picks_number = len(picks_list)
    total = book_number + picks_number
    context = {
        'book_list': book_list,
        'complete_link': complete_link,
        'book_number': book_number,
        'picks_list': picks_list,
        'picks_number': picks_number,
        'total_books': total,
    }

    return render(request, 'index.html', context)


def base(request):
    return render(request, 'base.html')


# manual addition of categories by rendering each page
def fantasy(request):
    link = 'https://manybooks.net/search-book?field_genre[17]=17'
    book_list = scrapper(link)
    # editors picks section below
    picks = 'https://manybooks.net/search-book?field_genre[38]=38'
    picks_list = scrapper(picks)
    complete_link = 'http://manybooks.net'
    book_number = len(book_list)
    picks_number = len(picks_list)
    total = book_number + picks_number
    context = {
        'book_list': book_list,
        'complete_link': complete_link,
        'book_number': book_number,
        'picks_list': picks_list,
        'picks_number': picks_number,
        'total_books': total,
    }
    return render(request, 'fantasy.html', context)


def categories(link, picks):
    book_list = scrapper(link)
    picks_list = scrapper(picks)
    book_number = len(book_list)
    picks_number = len(picks_list)
    total = book_number + picks_number
    complete_link = 'http://manybooks.net'
    context = {
        'book_list': book_list,
        'complete_link': complete_link,
        'book_number': book_number,
        'picks_list': picks_list,
        'picks_number': picks_number,
        'total_books': total,
    }
    return complete_link, context
def politics(request):
    link = 'https://manybooks.net/search-book?field_genre[22]=22'

    # editors picks section below
    picks = 'https://manybooks.net/search-book?field_genre[38]=38'



    }
    return render(request, 'politics.html', context)
