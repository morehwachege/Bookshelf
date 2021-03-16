from bs4 import BeautifulSoup
import requests
#add f_string to autogenerate the url

# link= 'https://manybooks.net/search-book?field_genre[30]=30'
#autogeneration code for the urls below
#page_id = 0
#while page_id <=100:
   # page_id += 1
   # link = f'https://manybooks.net/search-book?field_genre[{page_id}]={page_id}'
   # print(link)
#end of url autogeneration---uncomment when ready
def scrapper(link):
    source = requests.get(link)
    content = source.content

    soup = BeautifulSoup(content, 'lxml')
    item_list = []
    div = soup.find_all('article', class_='book')
    for link in div:
        a_tag = link.find('a')
        img = link.find('img', class_='img-responsive')
        crude = []
        if a_tag is not None:
            for shit in a_tag:
                crude.append(a_tag.attrs['href'])
                crude.append(img.attrs['src'])
                crude.append(img.attrs['alt'])
            item_list.append(crude)
        else:
            print('None Mfucker')

    return item_list

