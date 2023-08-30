import os
import numpy as np
import pandas as pd
import re 
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()



sns.set()

# Complete o código abaixo para realizar a leitura do arquivo
# o arquivo utiliza tabulação como separador
# dentro de strings a tabulação é represen tada como \t

df_muni_front = pd.read_csv('arq_municipios_fronteiricos.csv')
# Visualize as 5 primeiras linhas do DataFrame
print(df_muni_front.head(10))

# função que irá realizar o tratamento para um município
def tratar_nome_municipio(nome_municipio):
    #realize a limpeza
    nome_municipio_tratado = re.sub(r'([\d]* [–-] )(.*)', r'\2', nome_municipio)    
    return nome_municipio_tratado

# faça um teste de sua função para verificar se a transformação está correta
print(tratar_nome_municipio('1 - Aceguá'))

# aplique a função utilizando o método apply
municipios_tratados = df_muni_front['Município'].apply(tratar_nome_municipio)

# exiba todos os dados e verifique se o resultado está correto
print(municipios_tratados.head())

#algumas linhas ainda possuem hífen e números?
# problemas com caracteres são comuns
print(hex(ord('-'))) # código UTF8 do caracter (hexadecimal)
print(hex(ord('–'))) # código UTF8 do caracter (hexadecimal)
#'-' == '–'

# com todos os municípios devidamente tratados
# sobrescreva a coluna Município com os novos valores
df_muni_front.loc[:,'Município'] = municipios_tratados

# exiba as informações
print(df_muni_front.head(10))


# verifique os tipos das colunas do DataFrame. Utilize o método info(): 
df_muni_front.info()
         
def converter_para_float(texto):
        numero_float = float(texto)
        return numero_float

def converter_pib(texto):
    textoSemPonto = texto.replace('.', '').replace(' ','')
    numeroFloat = float(textoSemPonto)
    return numeroFloat


# aplique a função de conversão utilizando o método apply na coluna 'Área territorial'
area_territorial = df_muni_front['Área territorial'].apply(converter_para_float)
pib = df_muni_front['PIB (IBGE/2005'].apply(converter_pib)

# exiba alguns valores da com valores convertidos
print(area_territorial.head())
print(pib.head())

# substitua a coluna pelos valores convertidos
df_muni_front.loc[:, 'Área territorial'] = area_territorial


# faça o mesmo para a coluna PIB
df_muni_front.loc[:, 'PIB (IBGE/2005'] = pib
# imprima novamente as informações das colunas e verifique os tipos 
print(df_muni_front.info() )


# imprima novamente as primeiras linhas do DataFrame 
print(df_muni_front.head(60)) 

# crie o set e verifique o seu conteúdo
nomes_estados = set(df_muni_front['Estado'])

# exiba o set gerado
print(nomes_estados)

# crie o dicionário
dic_nomes_siglas = {
     'Acre':'AC',
     'Amapá':'AP',
     'Amazonas':'AM',
     'Mato Grosso':'MT',
     'Mato Grosso do Sul':'MS',
     'Paraná':'PR',
     'Pará':'PA',
     'Rio Grande do Sul':'RS',
     'Rondônia':'RO',
     'Roraima':'RR',
     'Santa Cataria':'SC',
     'Santa Catarina': 'SC'
}
# faça o mapeamento dos valores e atribua a : coluna_siglas_uf
coluna_siglas_uf = df_muni_front['Estado'].map(dic_nomes_siglas)

# verifique os 10 primeiros itens criados
print(coluna_siglas_uf.head(10))

# crie a coluna sigla 
df_muni_front['Sigla'] = coluna_siglas_uf 

# verifique as informações do dataframe 
print(df_muni_front.head())

# verifique quantos registros possuem o nome do estado de Santa Catarina escrito errado "Santa Cataria"
print(len(df_muni_front.loc[df_muni_front['Estado'] == 'Santa Cataria']))

# faça a correção dos registros que possuem o nome do estado de Santa Catarina escrito errado
df_muni_front.loc[df_muni_front['Estado'] == 'Santa Cataria', 'Estado'] = 'Santa Catarina'


# verifique, novamente, quantos registros possuem o nome do estado de Santa Catarina escrito errado
print(len(df_muni_front.loc[df_muni_front['Estado'] == 'Santa Cataria']))

# normalize a coluna PIB em quantidade de desvios padrão
pib_desvios = df_muni_front['PIB (IBGE/2005'].apply(lambda x: (x - df_muni_front['PIB (IBGE/2005'].mean())/df_muni_front['PIB (IBGE/2005'].std())

# exiba um histograma para as informações de PIB normalizado
plt.figure(figsize=(120,20))
sns.distplot(pib_desvios.dropna(), bins=20)
plt.xlabel('PIB (Quantidade de Desvios)')
plt.ylabel('Frequência')
plt.show()

# quais cidades possuem mais de 2 desvios 
df_muni_front['pib_desvios'] = pib_desvios
print(df_muni_front.loc[df_muni_front['pib_desvios'] > 2, ['Município','pib_desvios']])

# quantas cidades por estado?
print(df_muni_front.Sigla.value_counts())

# faça a ordenação do DataFrame pelo nome do município
print(df_muni_front.sort_values(by=['Município']))
# a ordenação está correta?









