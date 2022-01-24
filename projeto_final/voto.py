from datetime import date, datetime
import util

# constantes dados do eleitor
NOME = 0
MAE = 1
PAI = 2
NASCIMENTO = 3
TITULO = 4
VOTOU = 5
ANO_ATUAL = datetime.now().year

# constantes de situação do voto
OBRIGATORIO = 0
FACULTATIVO = 1
PROIBIDO = 2


def situacao_voto(idade):
    if idade in range(18, 70):
        return OBRIGATORIO
    elif idade >= 16:
        return FACULTATIVO
    return PROIBIDO


def validar_eleitor(dados_eleitor):
    util.titulo('VALIDAR ELEITOR')
    data_nascimento = dados_eleitor[NASCIMENTO]
    parte_data = data_nascimento.split('/')
    # converter para inteiros
    parte_data = [int(d) for d in parte_data]
    data = date(day=parte_data[0], month=parte_data[1], year=parte_data[2])
    # calcula a idade do eleitor
    idade = int((date.today() - data).days / 365)
    # usar função de validação
    print(f'Nome eleitor: {dados_eleitor[NOME]}')
    print(f'Titulo eleitor: {dados_eleitor[TITULO]}')
    print(f'Idade: {idade} anos')
    if situacao_voto(idade) == PROIBIDO:
        print(f'Com {idade} anos, seu voto é PROIBIDO!' )
    elif (situacao_voto(idade) == OBRIGATORIO and dados_eleitor == 'N'):
        print('VOCÊ NÃO ESTÁ QUITE, INVALIDADO!')
        return False
    else:
        print('ELEITOR VALIDADO, Pronto para emissão de Certificado.')
    return True




