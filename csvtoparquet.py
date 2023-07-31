import time
import pandas as pd
from pathlib import Path
#IMPRIME O HORÁRIO PARA CONTROLE
def imprime_time():
    localtime = time.localtime()
    result = time.strftime("%I:%M:%S %p", localtime)
    print(result)

arquivo_entrada = 'C:/Users/Leandro/projetos/teste-python/ruleskeywordscomsinonimos.csv'
arquivo_saida = 'C:/Users/Leandro/projetos/teste-python/ruleskeywordscomsinonimos.parquet'
print('path arquivo_entrada: ', Path(arquivo_entrada))

print('********************')
imprime_time()
print('antes da criacao do data frame')
print('********************')
arquivoentrada = pd.read_csv(arquivo_entrada,encoding='utf-8', delimiter=';')
print('********************')
imprime_time()
print('depois da criacao do df')
print('********************')
arquivoentrada.to_parquet(arquivo_saida)
print('********************')
imprime_time()
print('depois da criacao do parquet')
print('********************')
print('contagem de registros')
conteudo = '(media-only) & (alternative content) & (absence)'
coluna = 'Expressions'
# print(arquivoentrada[("ID")].count())
print(arquivoentrada[(arquivoentrada[coluna] == conteudo)].count())
# print(arquivo_entrada[(arquivo_entrada["tipo"] == "BODY")].count())
print('')
print('********************')
arquivo_entrada_parquet = 'C:/Users/Leandro/projetos/teste-python/ruleskeywordscomsinonimos.parquet'
print('path arquivo_entrada_parquet: ', Path(arquivo_entrada_parquet))
arquivo_entrada_parquet = pd.read_parquet(arquivo_entrada_parquet)
print('contagem de registros parquet')
# print(arquivo_entrada_parquet[("ID")].count())
print(arquivoentrada[(arquivoentrada[coluna] == conteudo)].count())
