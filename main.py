#Вариант 2
#задание 1
цены = [1200, 800, 1500, 950, 1100, 1300, 750, 900, 1050, 850, 950, 1200]

#хранение общей стоимости
общая_стоимость = 0

#Проходим по каждой цене в массиве и суммируем стоимость тех товаров, которые дороже 1000 рублей
for цена in цены:
    if цена > 1000:
        общая_стоимость += цена

print("Общая стоимость товаров дороже 1000 рублей:", общая_стоимость)

#задание 2
import numpy as np
массив = np.array([[10, 20, 30],
                   [40, 50, 60],
                   [70, 80, 90]])

# среднее значение элементов в массиве
среднее_значение = np.mean(массив)

# Инициализируем переменные для хранения координат элемента, наиболее близкого к среднему значению
ближайший_элемент = None
минимальная_разница = float('inf')

# Проходим по каждому элементу в массиве и сравниваем разницу со средним значением
for i in range(массив.shape[0]):
    for j in range(массив.shape[1]):
        разница = abs(массив[i, j] - среднее_значение)
        if разница < минимальная_разница:
            минимальная_разница = разница
            ближайший_элемент = (i, j)
print(f"Координаты элемента, наиболее близкого к среднему значению ({среднее_значение}): {ближайший_элемент}")

#задание 3
#список с некоторыми данными
список = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#перебор элементов списка
for элемент in список:
    if элемент % 2 == 0:  # Проверка элемента на четность
        print(элемент)

#задание 4
первый_список = [1, 2, 3, 4, 5]
второй_список = [3, 4, 5, 6, 7]

#списки в множества
множество_первого = set(первый_список)
множество_второго = set(второй_список)

#пересечение множеств и количество общих элементов
количество_общих = len(множество_первого.intersection(множество_второго))
print("Количество чисел, содержащихся одновременно в обоих списках:", количество_общих)

#задание 5

# словарь с парами слов
словарь = {
    "солнце": "свет",
    "дом": "жилище",
    "кошка": "кот",
    "стол": "таблица",
    "книга": "текст"
}

# Слово, для которого нужно найти синоним
искомое_слово = "книга"

# синоним в словаре
синоним = словарь.get(искомое_слово)
if синоним:
    print(f"Синоним слова '{искомое_слово}' - '{синоним}'")
else:
    print(f"Синоним для слова '{искомое_слово}' не найден в словаре.")

