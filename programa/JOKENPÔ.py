def mostra_linha():
    print('\033[1;33m' + '-=-' * 10 + '\033[0;0m')

    
mostra_linha()
print('\033[1;34m'+'PEDRA PAPEL E TESOURA')
mostra_linha()
import random
lista = ('[ 0 ] PEDRA', '[ 1 ] PAPEL', '[ 2 ] TESOURA')
for item in lista:
    print(f'\033[1;35m{item:^10}\033[m')
mostra_linha()
lista2 = ('PEDRA', 'PAPEL', 'TESOURA')
while True:

    while True:

        opção = int(input('Sua opção: '))
        computador = random.choice(lista2)
        conta = 2
        if opção == 0 and computador == 'PEDRA':
            print('\033[1;31mHOUVE UM EMPATE')
            if opção == 0:
                opção = 'PEDRA'
            elif opção == 1:
                opção = 'PAPEL'
            elif opção == 2:
                opção = 'TESOURA'
            mostra_linha()

            print('\033[1;34m' + f'COMPUTADOR = {computador}\nJOGADOR = {opção}')
        elif opção == 1 and computador == 'PAPEL':
            print('\033[1;31mHOUVE UM EMPATE')
            if opção == 0:
                opção = 'PEDRA'
            elif opção == 1:
                opção = 'PAPEL'
            elif opção == 2:
                opção = 'TESOURA'
            mostra_linha()

            print('\033[1;34m' + f'COMPUTADOR = {computador}\nJOGADOR = {opção}\033[m')
        elif opção == 2 and computador == 'TESOURA':
            print('\033[1;31mHOUVE UM EMPATE')
            if opção == 0:
                opção = 'PEDRA'
            elif opção == 1:
                opção = 'PAPEL'
            elif opção == 2:
                opção = 'TESOURA'

            mostra_linha()
            print('\033[1;34m' + f'COMPUTADOR = {computador}\nJOGADOR = {opção}')
        elif opção == 0 and computador == 'TESOURA':
            print('\033[1;32mO JOGADOR GANHOU! PARABÉNS!')
            break
        elif opção == 0 and computador == 'PAPEL':
            print('\033[1;31mO COMPUTADOR VENCEU! TENTE NOVAMENTE')
            break
        elif opção == 1 and computador == 'TESOURA':
            print('\033[1;31mO COMPUTADOR VENCEU! TENTE NOVAMENTE')
            break
        elif opção == 1 and computador == 'PEDRA':
            print('\033[1;32mO JOGADOR GANHOU! PARABÉNS!')
            break
        elif opção == 2 and computador == 'PEDRA':
            print('\033[1;31mO COMPUTADOR VENCEU! TENTE NOVAMENTE')
            break
        elif opção == 2 and computador == 'PAPEL':
            print('\033[1;32mO JOGADOR GANHOU! PARABÉNS!')
            break
        else:
            print('\033[1;31mOPÇÃO INVÁLIDA, TENTE NOVAMENTE!\033[m')
            conta += 2

    if opção==0:
        opção='PEDRA'
    elif opção==1:
        opção='PAPEL'
    elif opção==2:
        opção='TESOURA'
    mostra_linha()

    print('\033[1;34m' + f'COMPUTADOR = {computador}\nJOGADOR = {opção}\033[m')

    mostra_linha()
    break