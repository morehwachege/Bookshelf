from bs4 import BeautifulSoup
import requests

all_links = []
page_id = 0
while page_id <= 100:
    page_id += 1
    links = f"https://manybooks.net/search-book?language=All&field_genre%5B{page_id}%5D={page_id}&sticky=All&created_op=%3C&created%5Bvalue%5D=0&created%5Bmin%5D=&created%5Bmax%5D=&author_uid_op=%3E%3D&author_uid%5Bvalue%5D=0&author_uid%5Bmin%5D=&author_uid%5Bmax%5D=&sort_by=field_title"
    all_links.append(links)

for url in all_links:
    source = requests.get(url)
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
            print('Nothing To Display')
    print(item_list)
    print(page_id)