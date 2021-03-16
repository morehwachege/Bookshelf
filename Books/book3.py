from book_function import scrapper


link = 'https://manybooks.net/search-book?field_genre[30]=30'
escape_plan = scrapper(link)
print(escape_plan[0])