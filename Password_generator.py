import random

DIGITS = "0123456789"
LOWERCASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
PUNCTUATION = "!#$%&*+-=?@^_"
chars = ""
print("Добро пожаловать!")

def quan(quantity):
    return quantity.isdigit()


def qu_an():
    while True:
        quantity = input('Какое количество паролей нужно? ')
        if quan(quantity):
            return int(quantity)
        print('Может лучше целое число? ')

def llnn(ln):
    return ln.isdigit()


def l_n():
    while True:
        ln = input('Какую длинну одного пароля хочешь? ')
        if llnn(ln):
            return int(ln)
        print('Может лучше целое число? ')

def yes_no(answer):
    return answer.lower() in ('да', 'нет')

def ask_yes_no(prompt):
    while True:
        answer = input(prompt).lower()
        if answer in ('да', 'нет'):
            return answer
        print('Напишите только да или нет в нижнем регистре.')

if ask_yes_no(f'Добавлять {DIGITS}? ') == 'да':
    chars += DIGITS
if ask_yes_no(f'Добавлять {LOWERCASE_LETTERS}? ') == 'да':
    chars += LOWERCASE_LETTERS
if ask_yes_no(f'Добавлять {UPPERCASE_LETTERS}? ') == 'да':
    chars += UPPERCASE_LETTERS
if ask_yes_no(f'Добавлять {PUNCTUATION}? ') == 'да':
    chars += PUNCTUATION
if not chars:
    print('Нужно выбрать хотя бы один тип символов!')
else:
    quantity = qu_an()
    length = l_n()
    
    for _ in range(quantity):
        password = ''.join(random.choice(chars) for _ in range(length))
        print(password)