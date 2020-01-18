def get_cook_book(file_name):
    cook_book = {}
    
    with open(file_name) as f:        
        while True:
            key_name = f.readline().rstrip()            
            if not key_name:
                break
            items_count = int(f.readline().rstrip())          
            dish_list = []
            for foo in range(items_count):
                ingredient_list = f.readline().rstrip().split(' | ')
                if ingredient_list:
                    dish_list.append({'ingredient_name': ingredient_list[0],
                                    'quantity': ingredient_list[1],
                                    'measure': ingredient_list[2]
                    })
    
            f.readline().rstrip() 
            cook_book.setdefault(key_name, dish_list)
           
    return cook_book

def print_cook_book(book):
    for key in book:
        print(key)        
        [print(foo) for foo in book[key]]

def get_shop_list_by_dishes(dishes, person_count):
    ingredient_dict = {}
    cook_book = get_cook_book('cookbook.txt')
    for dish in dishes:
        for ingredient_list in cook_book[dish]:            
            if ingredient_list['ingredient_name'] not in ingredient_dict.keys():
                ingredient_dict.setdefault(ingredient_list['ingredient_name'], 
                                        {'measure': ingredient_list['measure'],
                                        'quantity': int(ingredient_list['quantity']) * person_count})
            else:
                ingredient_dict[ingredient_list['ingredient_name']]['quantity'] += \
                    int(ingredient_list['quantity']) * person_count

    return ingredient_dict

def print_shop_list_by_dishes(ingredients):
    [print(key, ': ', ingredients[key]) for key in ingredients]

import contextlib
from datetime import datetime
import sys
@contextlib.contextmanager
def log_open(path, method):
    try:
        file = open(path, method)        
        now = datetime.now()
        file.write(f'Запуск кода {str(now)}\n')
        yield file
    finally:
        now = datetime.now()
        exc_ex, exc_info, ex_tb = sys.exc_info()
        if ex_tb:
            file.write(f'  При исполнении кода возникла ошибка {ex_tb.tb_frame}: {exc_info}\n')
        file.write(f'Исполнение кода завершено {str(now)}\n\n')
        file.close()

if __name__ == '__main__':
    
    with log_open('log.txt', 'a') as log_file:

        print('Задача 1')
        print_cook_book(get_cook_book('cookbook.txt'))

        user_list = ['Запеченный картофель', 'Омлет']
        print(f"\nЗадача 2.1\nСоставляем список покупок для {user_list}")
        print_shop_list_by_dishes(get_shop_list_by_dishes(user_list, 2))

        user_list = ['Фахитос', 'Омлет']
        print(f"\nЗадача 2.2 c пересечением ингридиентов\nСоставляем список покупок для {user_list}")
        print_shop_list_by_dishes(get_shop_list_by_dishes(user_list, 2))
        1/0
    

