def des_linha(caracter='~', num=40):
    print(caracter * num)


def titulo(msg, n=40):
    des_linha()
    print(f'{msg:^{n}}')
    des_linha()


def leia_int(msg):
    while True:
        try:
            inteiro = int(input(msg))
        except (ValueError, TypeError, KeyboardInterrupt):
            print('ERRO! Entre com opção válida!')
        else:
            return inteiro


def menu(tupla, msg=' ', tamanho=40):
    titulo(msg, tamanho)
    ord = 1
    for opcao in tupla:
        print(f'{ord:>2} - {opcao}')
        ord += 1
    while True:
        des_linha()
        opc = leia_int('Digite opção: ')
        if opc in range(1, len(tupla)+1):
            break
        else:
            print(f'ERRO! Entre com 1 a {len(tupla)}')
    return opc