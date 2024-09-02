def fibonacci(num):
    a, b = 0, 1
    encontrou = False

    while a <= num:
        if a == num:
            encontrou = True
            break
        a, b = b, a + b
    
    if encontrou:
        print(f'O número {num} pertence a sequência de fibonacci!')
    else:
        print(f'O número {num} não pertence a sequência de fibonacci!')


escolha = int(input('Informe um número: '))
fibonacci(escolha)