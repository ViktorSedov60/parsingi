import re

import bs4

with open('index.html') as file:
    src = file.read()
# print(src)

soup = bs4.BeautifulSoup(src, 'lxml')


# # .find() .find_all
# page_h1 = soup.find('h1')
# print(page_h1)
#
# page2 = soup.find_all("h1")
# print(page2)
#
# for item in page2:
#     print(item.text)

# user_name = soup.find('div', class_='user__name')
# print(user_name)
# print(user_name.text)
# print(user_name.text.strip())

# user_name = soup.find('div', class_='user__name').find('span').text
# print(user_name)

# user_name = soup.find('div', {'class': 'user__name', 'id' :'aaa'}).find('span').text
# print(user_name)

# all_span = soup.find(class_='user__info').find_all('span')
# print(all_span)

# for item in all_span:
#     print(item.text)

# print(all_span[0])
# print(all_span[4].text)

# soc_link = soup.find(class_='social__networks'). find('ul').find_all('a')
# print(soc_link)

# all_a = soup.findAll('a')
# print(all_a)

# for item in all_a:
#     item_text = item.text
#     item_url = item.get('href')
#     print(f'{item_text}: {item_url}')

## metods:   .find_parent()   .find_parents()

# post_div = soup.find(class_='post__text').find_parent()
# print(post_div)

# post_div = soup.find(class_='post__text').find_parent('div', 'user__post')
# print(post_div)

# post_div = soup.find(class_='post__text').find_parents('div', 'user__post')
# print(post_div)


## metods .next_element    .previous_elevent
# next_el = soup.find(class_='post__title').next_element.next_element.text
# print(next_el)

# next_el = soup.find(class_='post__title').findNext().text
# print(next_el)

## metods:  find_next_sibling()    find_previous_sibling()
# next_sib = soup.find(class_='post__title').find_next_siblings()
# print(next_sib)

# prev_sib = soup.find(class_='post__date').find_previous_sibling()
# print(prev_sib)  ## ne rabotaet

# the_text = soup.find('a', text=re.compile('Одежда'))
## поиск по слову в контексте
# print(the_text)



