# 1 задание
#--------------------------------------------------------------------------------------------------------------------------------

import math
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

action = input("какое арифметическое действие вы хотите совершить?(/, *, -, +, %, //, **, factorial, fibonacci): ")

if action == "+":
    a=int(input("Chislo 1: "))
    b=int(input("Chislo 2: "))
    print(a+b)
if action == "-":
    a=int(input("Chislo 1: "))
    b=int(input("Chislo 2: "))
    print(a-b)
if action == "/":
    a=int(input("Chislo 1: "))
    b=int(input("Chislo 2: "))
    print(a/b)
if action == "*":
    a=int(input("Chislo 1: "))
    b=int(input("Chislo 2: "))
    print(a*b)
if action == "%":
    a=int(input("Chislo 1: "))
    b=int(input("Chislo 2: "))
    print(a%b)
if action == "//":
    a=int(input("Chislo 1: "))
    b=int(input("Chislo 2: "))
    print(a//b)
if action == "**":
    a=int(input("Chislo 1: "))
    b=int(input("Chislo 2: "))
    print(a**b)
if action == "factorial":
    a=int(input("Chislo: "))
    print(math.factorial(a))
if action == "fibonacci":
    a=int(input("Chislo: "))
    print(fib(a))
else:
    print("вы ввели что то не верно :(")




# 2 задание
#--------------------------------------------------------------------------------------------------------------------------------






board = [' ' for _ in range(9)]  

player1 = 'X'
player2 = 'O'
print("********** Игра Крестики-нолики для двух игроков **********")



while True:
    print('-------------')
    print('| ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' |')
    print('-------------')
    print('| ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' |')
    print('-------------')
    print('| ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' |')
    print('-------------')
    

    p = int(input('Куда поставим X? (введите числовую позицию от 0 до 8): '))
    board[p] = player1
    print('-------------')
    print('| ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' |')
    print('-------------')
    print('| ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' |')
    print('-------------')
    print('| ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' |')
    print('-------------')
    
    if board[0] == board[1] == board[2] == player1 or board[3] == board[4] == board[5] == player1 or board[6] == board[7] == board[8] == player1 or board[0] == board[3] == board[6] == player1 or board[1] == board[4] == board[7] == player1 or board[2] == board[5] == board[8] == player1 or board[0] == board[4] == board[8] == player1 or board[2] == board[4] == board[6] == player1:
        print('X выиграл!')
        break
    elif ' ' not in board:
        print('Ничья!')
        break
    
   

   
    p = int(input('Куда поставим O? (введите числовую позицию от 0 до 8): '))
    board[p] = player2
    print('-------------')
    print('| ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' |')
    print('-------------')
    print('| ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' |')
    print('-------------')
    print('| ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' |')
    print('-------------')
    
    if board[0] == board[1] == board[2] == player2 or board[3] == board[4] == board[5] == player2 or board[6] == board[7] == board[8] == player2 or board[0] == board[3] == board[6] == player2 or board[1] == board[4] == board[7] == player2 or board[2] == board[5] == board[8] == player2 or board[0] == board[4] == board[8] == player2 or board[2] == board[4] == board[6] == player2:
        print('O выиграл!')
        break
    elif ' ' not in board:
        print('Ничья!')
        break


    

# 3 задание
#--------------------------------------------------------------------------------------------------------------------------------



a = int(input("Количество голосующих: "))

kan = {"Аскаров" : 0, 
       "Бекмуханов" : 0,
        "Ернур" : 0, 
        "Пешая" : 0, 
        "Карим" : 0, 
        "Шаримазданов" : 0
}

print("Список кандидатов: " + ", ".join(kan.keys()))

i = 1
while i <= a:
    g=input("За кого вы голосуете?: ")
    if g in kan:
        i += 1
        kan[g] += 1
    else:
        print("Такого кандидата нет")

max_value = max(kan.values())


keys_with_max_values = []
for k,v in kan.items():
    if v == max_value:
        keys_with_max_values.append(k)

min_num_name = len(keys_with_max_values[0])
min_name = keys_with_max_values[0]
for k in keys_with_max_values:
    if min_num_name > len(k):
        min_num_name = len(k)
        min_name = k
print(kan)
print("Победитель " + min_name)