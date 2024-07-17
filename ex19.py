import random
a1 = input('informe o primeiro aluno: ')
a2 = input('informe o segundo aluno: ')
a3 = input('informe o terceiro aluno: ')
a4 = input('informe o quarto aluno: ')
lista = [a1,a2,a3,a4]
sorteio=random.choice(lista)
print('O aluno sorteado será {}'.format(sorteio))
