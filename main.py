import datetime as dt
from pip._vendor import requests
from io import BytesIO
import zipfile
from pathlib import Path
import pandas as pd
import os
import sys

#objeto que recebe a data de hoje.
hoje = dt.datetime.now().strftime('%Y-%m-%d')

#objeto que recebe o camminho da pasta com a data do dia.
pasta_raw = Path('.') / 'raw' / hoje

#objeto que recebe o caminho da nova pasta onde sera salvo o arquivo csv.
pasta_csv = 'swamp'

#objeto que recebe o caminho da pasta + o nome do arquivo csv.
pasta_arquivo_csv = os.path.join(pasta_csv, 'convertido.csv')

#objeto que recebe o nome da pasta que vai ser salvo o arquivo final.
pasta_lake = 'lake'

#Função que baixa um arquivo zip e extrai o conteúdo dentro de uma pasta.
def recebe_extrai_zip(site_loterias, pasta_extraida):
    r = requests.get(site_loterias, stream=True)
    z = zipfile.ZipFile(BytesIO(r.content))
    z.extractall(pasta_extraida)

#Função para criar uma pasta, caso ela não exista.
def criar_pasta(nome_pasta):
    if not os.path.exists(nome_pasta):
           os.mkdir(nome_pasta)

#Função que recebe um arquivo HTML e salva em CSV.
def converte_html(caminho_html, caminho_csv):
    
    #abre o arquivo html.
    df = pd.read_html(caminho_html, thousands='.', decimal='.')[0]
    
    #cria a pasta.
    criar_pasta(caminho_csv)
    
    #transoforma em csv.
    df.to_csv(caminho_csv + '\\convertido.csv', sep=';', index=False)

#função para ler o tratar o csv.
def lendo_csv(arquivo_csv, pasta_final):
    ler_csv = pd.read_csv(arquivo_csv, sep=';')
    
    #limpa os valores &nbsp da tabela.
    limpar_csv = ler_csv.apply(lambda x: x.replace('&nbsp', ''))
    
    #cria a pasta.
    criar_pasta (pasta_final)
    
    #salva o arquivo tratado dentro da pasta lake.
    limpar_csv.to_csv(pasta_final + '/tratado.csv', sep=';', index=False)

#objeto que recebe a lista de argumentos passados para o script.
arg = sys.argv

#passar o argumento megasena na posição 1.
if arg [1] == 'megasena':
        jogo = "http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_megase.zip"
        pasta_html = os.path.join(pasta_raw, 'd_mega.htm')
        recebe_extrai_zip(jogo, pasta_raw)
        converte_html (pasta_html, pasta_csv)
        lendo_csv(pasta_arquivo_csv, pasta_lake)

#passar o argumento quina na posição 1.        
elif arg [1] == 'quina':
        jogo = "http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_quina.zip"
        pasta_html = os.path.join(pasta_raw, 'd_quina.htm')
        recebe_extrai_zip(jogo, pasta_raw)
        converte_html (pasta_html, pasta_csv)
        lendo_csv(pasta_arquivo_csv, pasta_lake)

#passar o argumento lotofacil na posição 1.
elif arg [1] == 'lotofacil':
        jogo = "http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_lotfac.zip"
        pasta_html = os.path.join(pasta_raw, 'd_lotfac.htm')
        recebe_extrai_zip(jogo, pasta_raw)
        converte_html (pasta_html, pasta_csv)
        lendo_csv(pasta_arquivo_csv, pasta_lake)
