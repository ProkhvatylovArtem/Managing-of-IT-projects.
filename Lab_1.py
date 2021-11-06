"""
Завдання №3.4
Визначити нову стрічку hello. Здійснити операцію hello+ msg.
Змінити стрічку hello додавши в її кінці символ пробілу і знову виконати операцію hello+ msg.
"""
print('Завдання №3.4')

msg = 'Artem Prokhvatylov'
hello_string = 'Hello'
print(hello_string + msg)
hello_string = hello_string + ' '
print(hello_string + msg + '\n')


"""
Завдання №3.6
Визначити стрічку s=’colorless’. Використовуючи зрізи та операцію поєднання змінити стрічку до вигляду ‘colourless’.
"""
print('Завдання №3.6')

s = 'colorless'
print(s)
first_part = s[0:4]
second_part = s[4:9]
s = first_part + 'u' + second_part
print(s + '\n')


"""
Завдання №3.8
Спробуйте згенерувати IndexError доступаючись до символів стрічки з індексами менше 0.
"""
print('Завдання №3.8')

try:
    print(s[-1])
    print(s[-10])
    print(s[-11])
except IndexError:
    print('You can\'t get the index on the second round' + '\n')


"""
Завдання №3.14
Напишіть for цикл, який виведе на екран символи стрічки msg по одному на рядок.
"""
print('Завдання №3.14')

for i in msg:
    print(i)
print()


"""
Завдання №3.15
Створити список phrase1, який складається із значень ім’я , по батькові, прізвище студента. 
Що відбудеться при спробі ввести в інтерпретатор наступний оператор phrase1[2][2]. Поясніть результат.
"""
print('Завдання №3.15')

phrase1 = ['Artem', 'Sergiyovich', 'Prokhvatylov']

print(phrase1[2][2] + '\n')


"""
Завдання №3.23
Напишіть програму, яка надрукує слова із стрічки silly за абеткою.
"""
print('Завдання №3.23')

string = 'silly'
for i in ''.join(sorted(string)):
    print(i)
print()


"""
Завдання №3.24
Використайте функцію index() наступним чином ’inexpressible’.index(’e’).
Що станеться якщо виконати ’inexpressible’.index(’re’)
"""

print('Завдання №3.24')

print('inexpressible'.index('e'))
print('inexpressible'.index('re'))
print()
