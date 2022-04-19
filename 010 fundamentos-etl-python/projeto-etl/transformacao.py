#!/usr/bin/env python
# coding: utf-8

# # Notebook auxiliar para transformação de dados do projeto.ipynb
# ### Autora : Carla Edila Silveira
# ### Base: Base: Opendata AIG Brazil - acidentes aéreos do CENIPA

# ### EXTRAÇÃO DOS DADOS

# In[2]:


import pandas as pd #importa bilbioteca Pandas
import pandera as pa #importa biblioteca para montar esquema de validacao do dataframe


# In[3]:


valores_ausentes = ['**', '###!', '####', '***', '****', 'NULL'] #variavel recebe valores de dados ausentes
df = pd.read_csv("ocorrencia_2010_2020.csv", sep=";", parse_dates=['ocorrencia_dia'], dayfirst=True, na_values=valores_ausentes)
#extracao e leitura do dataframe com substituicao de dados nao disponíveis por NA para limpeza
df #carrega o dataframe


# ### VALIDAÇÃO DOS DADOS

# In[11]:


#bloco do esquema completo de validacao dos dados
#parametros das colunas devem ser compativeis com tipo de dados pra rodar a validacao
schema = pa.DataFrameSchema(  
    columns = {        
        "codigo":pa.Column(pa.Int, required=False),
        "codigo_ocorrencia":pa.Column(pa.Int), 
        "codigo_ocorrencia2":pa.Column(pa.Int),
        "ocorrencia_classificacao":pa.Column(pa.String),
        "ocorrencia_cidade":pa.Column(pa.String),
        "ocorrencia_uf":pa.Column(pa.String,pa.Check.str_length(2,2),nullable=True),
        "ocorrencia_aerodromo":pa.Column(pa.String, nullable=True),
        "ocorrencia_dia":pa.Column(pa.DateTime),
        "ocorrencia_hora":pa.Column(pa.String,pa.Check.str_matches(r'^([0-1]?[0-9]|[2][0-3]):([0-5][0-9])(:[0-5][0-9])?$'),
                                    nullable=True),
        "total_recomendacoes":pa.Column(pa.Int)                                               
    }
)


# In[12]:


schema.validate(df) #executa a validacao

#erros de validacao: inserido no esquema o nullable=True para colunas ocorr_uf e ocorr_aerodromo com dados null


# In[13]:


df.dtypes #verificacao de tipos de dados


# In[14]:


df.loc[1] #busca de dados por label da linha


# In[15]:


df.iloc[1] #busca de dados por índice da linha


# In[17]:


df.iloc[-1] #propriedade iloc busca dados da ultima linha do dataframe (ocorrencia 79844)


# In[18]:


df.tail() #confirmacao de ultima linha com tail


# In[19]:


df.iloc[10:15] #busca de fatias de dados pelo indice, range paralisa no indice 15(nao inclui os dados)


# In[20]:


df.loc[10:15] #busca de dados pelo label inclui a saída do último label do intervalo


# In[22]:


df.loc[:,'ocorrencia_uf'] #busca de dados por col. como numa matriz

#dois pontos indicam que sao todas as linhas, nome da col dá a localização


# In[23]:


df['ocorrencia_uf'] #busca (+ simples) dados da col informada sem referenciar linhas; mesmo resultado obtido com loc


# In[24]:


df.isna().sum() #mostra contagem de valores NA por coluna; funciona para todos NaN, NA, NaT


# In[25]:


df.isnull().sum() #outra opcao de mostrar contagem de NA por col


# In[26]:


filtro = df.ocorrencia_uf.isnull() #variavel recebe parametros da filtragem de nulos na col ocorr_uf
df.loc[filtro] #mostra dados NA da col conforme o filtro 


# In[29]:


filtro = df.ocorrencia_aerodromo.isnull() #variavel recebe parametros da filtragem de nulos em col aerodromo
df.loc[filtro] #mostra dados NA filtrados da col ocorr_aerodromo


# In[30]:


filtro = df.ocorrencia_hora.isnull() #variavel recebe parametros da filtragem de nulos em col hora
df.loc[filtro] #mostra dados filtrados da col ocorr_hora


# In[31]:


df.count() #mostra contagem de dados informados por col


# In[32]:


#ocorrencias com mais de 10 recomendacoes
filtro = df.total_recomendacoes > 10 #filtro recebe parametro
df.loc[filtro] #mostra resultado da filtragem do df


# In[35]:


filtro = df.total_recomendacoes > 10
df.loc[filtro, ['ocorrencia_cidade', 'total_recomendacoes']] 

#busca cidades com + mais 10 recomend. e total de recomend. de cada cidade


# In[40]:


#ocorrencias cuja classificacao == INCIDENTE GRAVE
filtro = df.ocorrencia_classificacao == 'INCIDENTE GRAVE' #compara classif. da col, atribui as buscas True ao filtro
df[filtro] #mostra as ocorrencias de INC. GRAVE com todas as informacoes


# In[41]:


#ocorrencias cuja classificacao == INCIDENTE GRAVE e o estado == SP
filtro1 = df.ocorrencia_classificacao == 'INCIDENTE GRAVE' #compara classif. da col, atribui as buscas True ao filtro
filtro2 = df.ocorrencia_uf == 'SP' #filtra ocorrencias do estado de SP
df[filtro1 & filtro2] #mostra o resultado da busca com combinacao de filtros  


# In[42]:


#ocorrencias cuja classificacao == INCIDENTE GRAVE ou o estado == SP
filtro1 = df.ocorrencia_classificacao == 'INCIDENTE GRAVE' #compara classif. da col, atribui as buscas True ao filtro
filtro2 = df.ocorrencia_uf == 'SP' #somente ocorrencias de SP
df[filtro1 | filtro2] #mostra resultado de buscas que atendem filtro 1 e filtro 2


# In[44]:


#ocorrencias cuja classificacao == INCIDENTE GRAVE ou classificacao == INCIDENTE e o estado == SP
filtro1 = (df.ocorrencia_classificacao == 'INCIDENTE GRAVE') | (df.ocorrencia_classificacao == 'INCIDENTE')
#compara classif. da col, atribui as buscas True ao filtro de opções condicionadas pelo operador ou (|)
filtro2 = df.ocorrencia_uf == 'SP'  #somente de SP
df[filtro1 & filtro2] #mostra resultados dos 2 filttos


# In[46]:


#funcao isin para filtrar ocorrencias cuja classif == INCIDENTE GRAVE ou classif == INCIDENTE e o estado == SP
filtro1 = df.ocorrencia_classificacao.isin(['INCIDENTE GRAVE', 'INCIDENTE']) #filtro com fç isin executa o OR 
filtro2 = df.ocorrencia_uf == 'SP' 2a opcao de filtro
df[filtro1 & filtro2] #mesmo resultado obtido no filtro com operador |


# In[49]:


#ocorrencias cujas cidades começam com letra P
filtro = df.ocorrencia_cidade.str[0] == 'P' #filtro busca 1o. caracter C dentro de strings da col ocorr_cidade
df.loc[filtro] #busca com filtro de strings


# In[50]:


#ocorrencias cujas cidades terminam com letra A
filtro = df.ocorrencia_cidade.str[-1] == 'A' #filtro pelo ultimo caracter A dentro de strings da col ocorr_cidade
df.loc[filtro]


# In[51]:


#ocorrencias cujas cidades terminam com caracteres NA
filtro = df.ocorrencia_cidade.str[-2:] == 'NA' #filtro pelo caracter NA do penultimo em diante dentro de strings
df.loc[filtro] #busca strings finalizadas com NA na col ocorr_cidade


# In[54]:


#ocorrencias cujas cidades contenham caracteres NA
filtro = df.ocorrencia_cidade.str.contains('NA')#filtro busca caracter NA dentro de qualquer parte das strings
df.loc[filtro] #busca de cidades com NA


# In[57]:


#ocorrencias cujas cidades contenham (em qualquer parte do conteúdo) caracteres NA ou AL
filtro = df.ocorrencia_cidade.str.contains('NA|AL')#filtro busca caracter NA ou AL  dentro de strings 
df.loc[filtro]


# In[58]:


#ocorrencias do ano de 2015
filtro = df.ocorrencia_dia.dt.year == 2015 #filtro busca datas de 2015
df.loc[filtro] #busca na col ocorr_dia


# In[61]:


#ocorrencias do ano de 2015 e mês 12
filtro1 = df.ocorrencia_dia.dt.year == 2015 #filtro busca datas de 2015
filtro2 = df.ocorrencia_dia.dt.month == 12 #busca datas de dezembro 
df.loc[filtro1 & filtro2] #busca com filtros combinados


# In[62]:


#opcao com filtro unico: ocorrencias do ano de 2015 e mês 12
filtro = (df.ocorrencia_dia.dt.year == 2015) & (df.ocorrencia_dia.dt.month == 12) #busca datas de dezembro de 2015
df.loc[filtro] #opcao de filtro com menos linhas código


# In[65]:


#ocorrencias do ano de 2015, mês 12 e dia 8
filtro_ano = df.ocorrencia_dia.dt.year == 2015 #filtro busca datas de 2015
filtro_mes = df.ocorrencia_dia.dt.month == 12 #busca datas de dezembro 
filtro_dia = df.ocorrencia_dia.dt.day == 8 #busca dia 8
df.loc[filtro_ano & filtro_mes & filtro_dia] #busca com 3 filtros combinados
#nao importa a ordem de filtros, resultado segue padrao apresentado no dataframe


# In[67]:


#ocorrencias do ano de 2015, mês 12 e dias entre 3 e 8
filtro_ano = df.ocorrencia_dia.dt.year == 2015 #filtro busca datas de 2015
filtro_mes = df.ocorrencia_dia.dt.month == 12 #busca datas de dezembro 
filtro_dia = (df.ocorrencia_dia.dt.day > 2) & (df.ocorrencia_dia.dt.day < 9) #busca dias 3 a 8
df.loc[filtro_ano & filtro_mes & filtro_dia] 

#1a execucao com erro de operador devido a falta de parentenses para separar parâmetros do filtro_dia 
#ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().


# In[73]:


df['ocorrencia_dia_hora'] = pd.to_datetime(df.ocorrencia_dia.astype(str) + ' ' + df.ocorrencia_hora)

#criacao de col para mostrar junto data e hora
#1a execucao falha por operacao com tipos de dados incompativeis
#TypeError: unsupported operand type(s) for +: 'DatetimeArray' and 'str'
#feita conversao de data em str para possibilitar concatenacao, seguida da conversao para data com metodo datetime


# In[74]:


df.head() #verificacao da inclusao da nova coluna dia+hora


# In[75]:


df.dtypes #cconferir transformacao de col dia_hora em tipo datetime


# In[77]:


#ocorrencias do ano de 2015, mês 12 e dias entre 3 e 8 (dia e hora juntas)
filtro_ano = df.ocorrencia_dia_hora.dt.year == 2015 #filtro busca datas de 2015
filtro_mes = df.ocorrencia_dia_hora.dt.month == 12 #busca datas de dezembro 
filtro_dia_inicio = df.ocorrencia_dia_hora.dt.day > 2 
filtro_dia_fim = df.ocorrencia_dia_hora.dt.day < 9 #busca dias 3 a 8
df.loc[filtro_ano & filtro_mes & filtro_dia_inicio & filtro_dia_fim] 


# In[78]:


#ocorrencias no periodo de 03/12/2015 11:00 até 08/12/2015 14:30
filtro1 = df.ocorrencia_dia_hora >= '2015-12-03 11:00:00'
filtro2 = df.ocorrencia_dia_hora <= '2015-12-08 14:30:00'
df.loc[filtro1 & filtro2] #busca ocorrencias do filtro por periodo (com data e hora)


# In[79]:


#ocorrencias do ano de 2015 e mês 3
filtro1 = df.ocorrencia_dia.dt.year == 2015 #filtro busca datas de 2015
filtro2 = df.ocorrencia_dia.dt.month == 3 #busca datas de março
df201503 = df.loc[filtro1 & filtro2] #criado novo dataframe
df201503  #mostra dataframe tranformado


# In[80]:


df201503.count() #contagem de ocorrencias do novo dataframe

#tomar cuidado com agrupamento por col com dados NA, como ocorr_aerodromo (menos dados que demais col)


# In[81]:


df201503.groupby(['codigo_ocorrencia']).count() #contagem de dados mediante agrupamento

#definir a col pra fazer agrupamento com base no count do dataframe


# In[82]:


df201503.groupby(['codigo_ocorrencia']).codigo_ocorrencia.count()#agrupamento por cod_ocorrencia

#contagem por cod_ocorrencia


# In[83]:


df201503.groupby(['ocorrencia_classificacao']).codigo_ocorrencia.count() #agrupamento de classif por cod_ocorr

#contagem por ocorr_classificacao


# In[87]:


df201503.groupby(['ocorrencia_classificacao']).ocorrencia_aerodromo.count()

#agrupamento de ocorr_classificacao por aerodromo demonstra menos dados


# In[84]:


df201503.groupby(['ocorrencia_aerodromo']).codigo_ocorrencia.count()

#contagem por ocorr_aerodromo dá diferença em relação à classificacao de ocorrencias
#contagem por col com dados nulos fica equivocada no agrupamento


# In[88]:


df201503.groupby(['ocorrencia_classificacao']).size() #size agrupa e conta os registros/linhas agrupados na col

#contagem inclui dados NA


# In[91]:


df201503.groupby(['ocorrencia_classificacao']).size().sort_values() #agrupa em ordem ascendente 


# In[90]:


df201503.groupby(['ocorrencia_classificacao']).size().sort_values(ascending=False) #agrupa em ordem descendente


# In[92]:


#filtragem de dados de ocorrencia da regiao sudeste
filtro1 = df.ocorrencia_dia.dt.year == 2010  #filtra ocorrencias por ano
filtro2 = df.ocorrencia_uf.isin(['SP', 'MG', 'ES', 'RJ']) #filtra ocorrencias por regiao na col ocorr_uf
dfsudeste2010 = df.loc[filtro1 & filtro2] #busca de dados dos filtros combinados
dfsudeste2010 #imprime novo dataframe


# In[93]:


dfsudeste2010.groupby(['ocorrencia_classificacao']).size() #agrupa ocorrencias por classificaçao 


# In[94]:


dfsudeste2010.count() #contagem de ocorrencias do dataframe por col


# In[95]:


dfsudeste2010.groupby(['ocorrencia_classificacao', 'ocorrencia_uf']).size() 

#agrupamento de classificacao por UF da regiao


# In[96]:


dfsudeste2010.groupby(['ocorrencia_uf', 'ocorrencia_classificacao']).size() 

#agrupamento de UF por classificacao de ocorrencias


# In[98]:


dfsudeste2010.groupby(['ocorrencia_cidade']).size().sort_values(ascending=False) 

#agrupamento de ocorrencia das cidade da regiao sudeste em ordem descencente


# In[100]:


filtro = dfsudeste2010.ocorrencia_cidade =='RIO DE JANEIRO' 
dfsudeste2010.loc[filtro] #filtra ocorrencias da cidade do Rio de Janeiro


# In[101]:


filtro = dfsudeste2010.ocorrencia_cidade =='RIO DE JANEIRO' 
dfsudeste2010.loc[filtro].total_recomendacoes.sum() #soma de recomendacoes do Rio de Janeiro


# In[103]:


filtro1 = dfsudeste2010.ocorrencia_cidade =='RIO DE JANEIRO' 
filtro2 = dfsudeste2010.total_recomendacoes > 0 
dfsudeste2010.loc[filtro1 & filtro2] #imprime resultado para conferir com soma anterior


# In[104]:


dfsudeste2010.groupby(['ocorrencia_cidade']).total_recomendacoes.sum()

#agrupamento do total de ocorrencias por cidade, indenpendente de haver ou nao recomendacoes


# In[107]:


dfsudeste2010.groupby(['ocorrencia_aerodromo'], dropna=False).total_recomendacoes.sum()

#agrupamento do total de ocorrencias por aerodromo, incluindo dados NA 


# In[108]:


filtro = dfsudeste2010.total_recomendacoes > 0 #filtra cidades com recomendacoes em ordem ascendente
dfsudeste2010.loc[filtro].groupby(['ocorrencia_cidade']).total_recomendacoes.sum().sort_values()


# In[109]:


dfsudeste2010.loc[filtro].groupby(['ocorrencia_cidade', dfsudeste2010.ocorrencia_dia.dt.month]).total_recomendacoes.sum()

#agrupamento de cidades por ocorr diaria e total de recomendacoes


# In[111]:


filtro1 = dfsudeste2010.total_recomendacoes > 0 #filtra ocorrencias com recomendacoes da regiao
filtro2 = dfsudeste2010.ocorrencia_cidade == 'SÃO PAULO' #filtra ocorrencias de Sao Paulo
dfsudeste2010.loc[filtro1 & filtro2] #busca combinada de filtros