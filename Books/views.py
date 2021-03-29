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

def politics(request):
    link = 'https://manybooks.net/search-book?field_genre[22]=22'
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

def thriller(request):
    link = 'https://manybooks.net/search-book?field_genre[66]=66'
    book_list = scrapper(link)
    # editors picks section below
    picks = 'https://manybooks.net/search-book?field_genre[17]=17'
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
    return render(request, 'thriller.html', context)


def mystery(request):
    link = 'https://manybooks.net/search-book?field_genre[19]=19'
    book_list = scrapper(link)
    # editors picks section below
    picks = 'https://manybooks.net/search-book?field_genre[17]=17'
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
    return render(request, 'mystery.html', context)


def children(request):
    link = 'https://manybooks.net/search-book?field_genre[14]=14'
    book_list = scrapper(link)
    # editors picks section below
    picks = 'https://manybooks.net/search-book?field_genre[15]=15'
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
    return render(request, 'children.html', context)

def humour(request):
    link = 'https://manybooks.net/search-book?field_genre[28]=28'
    book_list = scrapper(link)
    # editors picks section below
    picks = 'https://manybooks.net/search-book?field_genre[26]=26'
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
    return render(request, 'humour.html', context)


def pirate(request):
    link = 'https://manybooks.net/search-book?field_genre[62]=62'
    book_list = scrapper(link)
    # editors picks section below
    picks = 'https://manybooks.net/search-book?field_genre[63]=63'
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
    return render(request, 'pirate.html', context)

def ghost(request):
    link = 'https://manybooks.net/search-book?field_genre[60]=60'
    book_list = scrapper(link)
    # editors picks section below
    picks = 'https://manybooks.net/search-book?field_genre[59]=59'
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
    return render(request, 'ghost.html', context)

def havard(request):
    link = 'https://manybooks.net/search-book?field_genre[11]=11'
    book_list = scrapper(link)
    # editors picks section below
    picks = 'https://manybooks.net/search-book?field_genre[12]=12'
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
    return render(request, 'havard.html', context)


def health(request):
    link = 'https://manybooks.net/search-book?field_genre[58]=58'
    book_list = scrapper(link)
    # editors picks section below
    picks = 'https://manybooks.net/search-book?field_genre[59]=59'
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
    return render(request, 'health.html', context)

def african(request):
    link = 'https://manybooks.net/search-book?field_genre[52]=52'
    book_list = scrapper(link)
    # editors picks section below
    picks = 'https://manybooks.net/search-book?field_genre[53]=53'
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
    return render(request, 'african.html', context)


def adventure(request):
    link = 'https://manybooks.net/search-book?field_genre[10]=10'
    book_list = scrapper(link)
    # editors picks section below
    picks = 'https://manybooks.net/search-book?field_genre[57]=57'
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
    return render(request, 'adventure.html', context)