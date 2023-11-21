import os
from pprint import pprint

file_path = os.path.join(os.getcwd(), 'recipes.txt')

with open(file_path, 'r', encoding='utf-8') as f:
    """
    - создаем словарь, содержащий ключ
    - получаем ключ из строки и прописываем кол-во ингредиентов
    - создаем список ингредиентов
    - прописываем название, кол-во и единицу измерения ингредиентов
    - добавляем ингредиенты в список
    - добавляем ключи в словарь
    - readline() для чтения пустой строки
    - выводим словарь
    """

    cook_book = {}
    for string in f:
        dish = string.strip()
        ingredients = int(f.readline().strip())
        book = []
        for value in range(ingredients):
            ingredient_name, quantity, measure = f.readline().strip().split('|')
            book.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        cook_book[dish] = book
        f.readline()
    pprint(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    """Принимает список блюд из словаря и количество персон, для кого будем готовить"""
    list_dishes = {}
    for d in dishes:
        for ingredient in cook_book[d]:
            new_shop_list_item = dict(ingredient)
            new_shop_list_item['quantity'] = int(new_shop_list_item['quantity']) * person_count
            if new_shop_list_item['ingredient_name'] not in list_dishes:
                list_dishes[new_shop_list_item['ingredient_name']] = new_shop_list_item
            else:
                list_dishes[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item['quantity']
    return list_dishes


shop_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

pprint(shop_list)
