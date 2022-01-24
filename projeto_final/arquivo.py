import os
from datetime import date, datetime
import util

NOME = 0
MAE = 1
PAI = 2
NASCIMENTO = 3
TITULO = 4
VOTOU = 5
ANO_ATUAL = datetime.now().year

substituicoes = ['$NOME$',
                 '$MAE$',
                 '$PAI$',
                 '$NASC$',
                 '$TITULO$'
                ]

PATH_REL = 'projeto_final'
NOVA_CERTIDAO = os.path.join(PATH_REL, 'dados', 'certidao_emitida.html')

def ler_arquivo(caminho):
    f = open(caminho)
    conteudo = f.read()
    f.close()
    return conteudo


def existe_arquivo(caminho):
    if os.path.exists(caminho):
        return True
    else:
        return False


def criar_arquivo(caminho):
    try:
        f = open(caminho, 'wt+')
    except:
        return False
    else:
        f.close()
        return True


# TODO: zona; secao; municipio; uf; data_insc;
def criar_base_eleitores(caminho):
    campos = ('NOME', 'MAE', 'PAI', 'DTA_NASC', 'TITULO', 'VOTOU')
    # Criar a base de dados de eleitores
    f = open(caminho, 'wt+')
    linha = ';'.join(campos)
    f.write(linha + '\n')
    f.close()


def cadastrar_eleitor():
    util.titulo('CADASTRAR ELEITOR')
    nome = str(input('Nome eleitor: ')).strip().upper()
    mae = str(input('Nome da mãe: ')).strip().upper()
    pai = str(input('Nome do pai: ')).strip().upper()
    dta_nasc = str(input('Data Nascimento: ')).strip()
    titulo = util.leia_int('Titulo de Eleitor: ')
    votou = str(input('Votou na última eleição? [S/N]: ')).strip().upper()[0]
    dados = (nome, mae, pai, dta_nasc, str(titulo), votou)
    return dados


def gravar_eleitor(dados, caminho):
    try:
        f = open(caminho, 'a')
    except:
        return False
    else:
        linha = ';'.join(dados)
        f.write(linha + '\n')
        f.close()
        return True
 

def solicitar_dados_busca():
    nome = str(input('Nome do eleitor: ')).strip().upper()
    titulo = util.leia_int('Titulo de Eleitor: ')
    dados = (nome, str(titulo))
    return dados


def buscar_eleitor(dados, caminho):
    f = open(caminho)
    linhas = f.readlines()
    f.close()
    for linha in linhas:
        dados_eleitor = linha.split(';')
        # busca nome e titulo em cada linha
        if (dados[0] == dados_eleitor[NOME] and dados[1] == dados_eleitor[TITULO]):
            return dados_eleitor
    return []


def emitir_certificado(dados, caminho):
    util.titulo('EMITIR CERTIFICADO')
    f = open(caminho, 'r')
    conteudo = f.read()
    f.close()
    for i in range(len(substituicoes)):
        conteudo = conteudo.replace(substituicoes[i], dados[i])
    # Substituir data e hora
    agora = datetime.now()
    conteudo = conteudo.replace('$DATA$', agora.date().strftime('%d/%m/%Y'))
    conteudo = conteudo.replace('$HORA$', str(agora.time().strftime('%H:%M:%S')))
    f = open(NOVA_CERTIDAO, 'w+')
    f.write(conteudo)
    f.close()
    print('Certificado Emitido')

    