'''
JOKENPÔ versão PEDRA | PAPEL | TESOURA | LAGARTO | SPOCK
"Rock Paper Scissors Lizard Spock" by Sam Kass and Karen Bryla
v.1.0
14/03/2022
---------------------------------------------------------------
REGRAS:
- Tesoura corta papel
- Papel cobre pedra
- Pedra esmaga lagarto
- Lagarto envenena Spock
- Spock derrete tesoura
- Tesoura decapita lagarto
- Lagarto come papel
- Papel refuta Spock
- Spock vaporiza pedra
- Pedra amassa tesoura
'''

from random import randint
from time import sleep
import sys

item = ('Pedra', 'Papel', 'Tesoura', 'Lagarto', 'Spock')
comp = randint(0, 4)

print('\n-------------------------- JOKENPÔ ----------------------------')
print('---------- PEDRA | PAPEL | TESOURA | LAGARTO | SPOCK ----------')

print('''\nOPÇÕES:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
[ 3 ] LAGARTO
[ 4 ] SPOCK
[ 5 ] SAIR''')

jogador = int(input('\nEscolha sua jogada: '))

while jogador != 0 and jogador != 1 and jogador != 2 and jogador != 3 and jogador != 4 and jogador != 5:
    print('Opção inválida!')
    jogador = int(input('Escolha sua jogada: \n'))

if jogador == 5:
    print('Vida longa e próspera!')
    sys.exit()

print('\033[34mJO', end='')
sleep(0.5)
print('KEN', end='')
sleep(0.5)
print('PÔ!')
sleep(0.5)

print('\033[m-' * 42)
print('Computador escolheu: \033[33m{}'.format(item[comp]))
print('\033[mJogador escolheu: \033[33m{}'.format(item[jogador]))
print('\033[m-' * 42)

if comp == 0:
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Papel cobre a pedra. \033[1:32mJogador venceu\033[m')
    elif jogador == 2:
        print('Pedra amassa tesoura. \033[1:32mComputador venceu\033[m')
    elif jogador == 3:
        print('Pedra esmaga lagarto. \033[1:32mComputador venceu\033[m')
    elif jogador == 4:
        print('Spock vaporiza a pedra. \033[1:32mJogador venceu\033[m')

elif comp == 1:
    if jogador == 0:
        print('Papel cobre a pedra. \033[1:32mComputador venceu\033[m')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Tesoura corta papel. \033[1:32mJogador venceu\033[m')
    elif jogador == 3:
        print('Lagarto come papel. \033[1:32mJogador venceu\033[m')
    elif jogador == 4:
        print('Papel refuta Spock. \033[1:32mComputador venceu\033[m')

elif comp == 2:
    if jogador == 0:
        print('Pedra amassa tesoura. \033[1:32mJogador venceu\033[m')
    elif jogador == 1:
        print('Tesoura corta papel. \033[1:32mComputador venceu\033[m')
    elif jogador == 2:
        print('Empate')
    elif jogador == 3:
        print('Tesoura decapita lagarto. \033[1:32mComputador venceu\033[m')
    elif jogador == 4:
        print('Spock derrete tesoura. \033[1:32mJogador venceu\033[m')

elif comp == 3:
    if jogador == 0:
        print('Pedra esmaga lagarto. \033[1:32mJogador venceu\033[m')
    elif jogador == 1:
        print('Lagarto come papel. \033[1:32mComputador venceu\033[m')
    elif jogador == 2:
        print('Tesoura decapita lagarto. \033[1:32mJogador venceu\033[m')
    elif jogador == 3:
        print('Empate')
    elif jogador == 4:
        print('Lagarto envenena Spock. \033[1:32mComputador venceu\033[m')

elif comp == 4:
    if jogador == 0:
        print('Spock vaporiza pedra. \033[1:32mComputador venceu\033[m')
    elif jogador == 1:
        print('Papel refuta Spock. \033[1:32mJogador venceu\033[m')
    elif jogador == 2:
        print('Spock derrete tesoura. \033[1:32mComputador venceu\033[m')
    elif jogador == 3:
        print('Lagarto envenena Spock. \033[1:32mJogador venceu\033[m')
    elif jogador == 4:
        print('Empate')

print('-' * 42)
