#1. Используя функцию map() для переписывания цикла:
"""
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
print("Squared list:", squared)

#2. Используя функцию reduce() для переписывания цикла:

list = [1, 2, 3, 4]
product = reduce(lambda x, y: x*y, list)
print("Product:", product)

#3. Используя функцию map() для переписывания цикла:

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)

#4. Объединение списков x и y с помощью функции zip():

x = [1, 2, 3]
y = [4, 5, 6]
result = list(zip(x, y))
print(result)
"""
#5. Использование функции zip() для переписывания цикла:

name_hero = [
    'Hulk',
    'Mr. Fantastic',
    'Invisible Woman',
    'Doctor Strange',
    'Doctor Octopus',
    'Spider-Man',
]

name_real = [
    'Bruce Banner',
    'Reed Richards',
    'Sue Storm',
    'Stephen Strange',
    'Otto Octavius',
    'Peter Parker',
]

for hero, real_name in zip(name_hero, name_real):
    print(hero, '-', real_name)

#6. Использование функции filter() для перемещения нечетных элементов списка в новый список:

numbers = [1, 2, 4, 5, 7, 8, 10, 11]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)