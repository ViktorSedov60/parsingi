import random
from time import sleep

import bs4
import requests
import json
import csv

# url = "https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"
#
headers= {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.141 YaBrowser/22.3.3.852 Yowser/2.5 Safari/537.36"
}
#
# req = requests.get(url)
# src = req.text
# # print(src)
#
# with open("index.html", "w", encoding="UTF-8") as file:
#     file.write(src)

# with open("index.html", encoding="UTF-8") as file:
#     src = file.read()
#
# soup = bs4.BeautifulSoup(src, "lxml")
# all_prod = soup.findAll(class_="mzr-tc-group-item-href")
#
# all_prod_dict = {}
# for item in all_prod:
#     item_text = item.text
#     item_href = "https://health-diet.ru" + item.get("href")
#     # print(f"{item_text}: {item_href}")
#     all_prod_dict[item_text] = item_href

# with open("all_prod_dict.json", "w", encoding="UTF-8") as file:
#     json.dump(all_prod_dict, file, indent=4, ensure_ascii=False)

with open("all_prod_dict.json", encoding="UTF-8") as file:
    all_prod = json.load(file)
# print(all_prod)

iteration_count = int(len(all_prod)) - 1
count = 0
print(f"Всего итераций :{iteration_count}")
for category_name, category_href in all_prod.items():

## меняем знаки в полученном словаре для дальнейшуй работы

    rep = [",", " ", "-", "'"]
    for item in rep:
        if item in category_name:
            category_name = category_name.replace(item, "_")
    # print(category_name)

    req = requests.get(url=category_href, headers=headers)
    src = req.text

    with open(f"data/{count}_{category_name}.html" , "w", encoding="UTF-8")as file:
        file.write(src)

    with open(f"data/{count}_{category_name}.html", encoding="UTF-8")as file:
        src = file.read()

    soup = bs4.BeautifulSoup(src, "lxml")

## проверка страницы на наличие таблицы с продуктами
    alert_block = soup.find(class_="uk-alert-danger")
    if alert_block is not None:
        continue




    ## собираем заголовки
    tabl_head = soup.find(class_="mzr-tc-group-table").find("tr").find_all("th")
    # print(tabl_head)
    product = tabl_head[0].text
    calories = tabl_head[1].text
    proteins = tabl_head[2].text
    fats = tabl_head[3].text
    carbohydrates = tabl_head[4].text

    with open(f"data/{count}_{category_name}.csv", "w", encoding="UTF-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                product,
                calories,
                proteins,
                fats,
                carbohydrates

            )
        )


## собираем данные продуктов
    product_data = soup.find(class_="mzr-tc-group-table").find("tbody").find_all("tr")

    product_info = []

    for item in product_data:
        product_tds = item.find_all("td")

        title = product_tds[0].find("a").text
        # print(title)
        calories = product_tds[1].text
        proteins = product_tds[2].text
        fats = product_tds[3].text
        carbohydrates = product_tds[4].text
        # print(proteins)

        product_info.append(
            {
                "Title": title,
                "Calories": calories,
                "Proteins": proteins,
                "Fats": fats,
                "Carbohydrates": carbohydrates

            }
        )

        with open(f"data/{count}_{category_name}.csv", "a", encoding="UTF-8") as file:
            writer = csv.writer(file)
            writer.writerow(
                (
                    title,
                    calories,
                    proteins,
                    fats,
                    carbohydrates

                )
            )

    with open(f"data/{count}_{category_name}.csv", "a", encoding="UTF-8") as file:
        json.dump(product_info, file, indent=4, ensure_ascii=False)

    count += 1
    print(f"итерация {count}. {category_name} записан...")
    iteration_count = iteration_count - 1

    if iteration_count == 0:
        print("Забота завершена")
        break

    print(f"осталось итераций : {iteration_count}")
    sleep(random.randrange(2, 4))