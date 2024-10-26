# questao 1
print('QUESTAO 1')
def fibonacci(n):
    a, b = 0, 1
    while True:
        if n == b or n == 0:
            print('O numero faz parte da Sequencia de Fibonacci')
            break
        elif n < b:
            print('O numero não faz parte da Sequencia de Fibonacci')
            break
        c = a + b
        a, b = b, c

numero = int(input('Insira um numero inteiro: '))
fibonacci(numero)


# questao 2
print('\nQUESTAO 2')
def verificar_string(letra, palavra):
    contagem = 0
    for caracter in palavra.lower():
        if caracter == letra:
            contagem += 1
    if contagem == 0:
        print(f'A letra {letra} não se encontra na string {palavra}')
    else:
        print(f'A letra {letra} aparece {contagem} vezes na string {palavra}')

palavra = input('Digite algo: ')
verificar_string('a', palavra)


# questao 3
print('\nQUESTAO 3')
indice = 12
soma = 0
k = 1
while k < indice:
    k += 1
    soma += k
print('o resultado de k vai ser 77')
print(k)
