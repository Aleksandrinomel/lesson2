'''
1) Создать список с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
2) Посчитать и вывести средний балл по всей школе.
3) Посчитать и вывести средний балл по каждому классу.
'''


import random

# Генератор списка: класс - оценки.
list_rating = [{'school_class': str(i) + j, 'scores': [random.randint(1, 5) for _ in range(random.randint(20, 30))]} for
               j in ["а", "б", "в", "г"] for i in range(1, 12)]

rating_sum, amount = 0, 0
for sch_class in range(len(list_rating)):
    amount += len(list_rating[sch_class]['scores'])
    rating_sum += sum(list_rating[sch_class]['scores'])
    print('Средний балл класса', list_rating[sch_class]['school_class'], ': ',
          int(sum(list_rating[sch_class]['scores']) / len(list_rating[sch_class]['scores'])))
print('Средний балл по школе: ', int(rating_sum / amount))
