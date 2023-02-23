um = 0
dois = 0
tres = 0
quatro = 0
cinco = 0
seis = 0
sete = 0
oito = 0
nove = 0

umt = 1
doist = 2
trest = 3
quatrot = 4
cincot = 5
seist = 6
setet = 7
oitot = 8
novet = 9

print(f'[{umt}][{doist}][{trest}]')
print(f'[{quatrot}][{cincot}][{seist}]')
print(f'[{setet}][{oitot}][{novet}]')

for i in range(5):

    while True:
        jogadorx = int(input ('Jogador X digite um número de 1 a 9: '))

        
        if jogadorx == 1 and um == 0:
            umt = 'X'
            um = 1
            break
        if jogadorx == 2 and dois == 0:
            doist = 'X'
            dois = 1
            break
        if jogadorx == 3 and tres == 0:
            trest = 'X'
            tres = 1
            break
        if jogadorx == 4 and quatro == 0:
            quatrot = 'X'
            quatro = 1
            break
        if jogadorx == 5 and cinco == 0:
            cincot = 'X'
            cinco = 1
            break
        if jogadorx == 6 and seis == 0:
            seist = 'X'
            seis = 6
            break
        if jogadorx == 7 and sete == 0:
            setet = 'X'
            sete = 7
            break
        if jogadorx == 8 and oito == 0:
            oitot = 'X'
            oito = 1
            break
        if jogadorx == 9 and nove == 0:
            novet = 'X'
            nove = 1
            break

    print(f'[{umt}][{doist}][{trest}]')
    print(f'[{quatrot}][{cincot}][{seist}]')
    print(f'[{setet}][{oitot}][{novet}]')

    #verifica todas as linhas se o jogador X ganhou
    if um + dois + tres == 3 or quatro + cinco + seis == 3 or sete + oito + nove == 3:
        print('Jogador X ganhou!')
        break

    #verifica todas as colunas se o jogador X ganhou
    if um + quatro + sete == 3 or dois + cinco + oito == 3 or tres + seis + nove == 3:
        print('Jogador X ganhou!')
        break

    #verifica todas as diagonais se o jogador X ganhou
    if um + cinco + nove == 3 or tres + cinco + sete == 3:
        print('Jogador X ganhou!')
        break

    # empate
    if um != 0 and dois != 0 and tres != 0 and quatro != 0 and cinco != 0 and seis != 0 and sete != 0 and oito != 0 and nove != 0:
        print('Deu velha!!!')
        break

    while True:
        jogadoro = int(input ('Jogador O digite um número de 1 a 9: '))

        if jogadoro == 1 and um == 0:
            umt = 'O'        
            um = -1
            break
        if jogadoro == 2 and dois == 0:
            doist = 'O'
            dois = -1
            break
        if jogadoro == 3 and tres == 0:
            trest = 'O'
            tres = -1
            break
        if jogadoro == 4 and quatro == 0:
            quatrot = 'O'
            quatro = -1
            break
        if jogadoro == 5 and cinco == 0:
            cincot = 'O'
            cinco = -1
            break
        if jogadoro == 6 and seis == 0:
            seist = 'O'
            seis = -1
            break
        if jogadoro == 7 and sete == 0:
            setet = 'O'
            sete = -1
            break
        if jogadoro == 8 and oito == 0:
            oitot = 'O'
            oito = -1
            break
        if jogadoro == 9 and nove == 0:
            novet = 'O'
            nove = -1
            break

    print(f'[{umt}][{doist}][{trest}]')
    print(f'[{quatrot}][{cincot}][{seist}]')
    print(f'[{setet}][{oitot}][{novet}]')

    #verifica todas as linhas se o jogador O ganhou
    if um + dois + tres == -3 or quatro + cinco + seis == -3 or sete + oito + nove == -3:
        print('Jogador O ganhou!')
        break

    #verifica todas as colunas se o jogador O ganhou
    if um + quatro + sete == -3 or dois + cinco + oito == -3 or tres + seis + nove == -3:
        print('Jogador O ganhou!')
        break

    #verifica todas as diagonais se o jogador O ganhou
    if um + cinco + nove == -3 or tres + cinco + sete == -3:
        print('Jogador O ganhou!')
        break
    


