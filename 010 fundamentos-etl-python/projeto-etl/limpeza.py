#!/usr/bin/env python
# coding: utf-8

# # **Notebook auxiliar para etapa de limpeza do projeto.ipynb**
# ### Autora: Carla Edila Silveira
# ### Base: Opendata AIG Brazil - acidentes aéreos do CENIPA

# ### MANIPULAÇÃO DO DATAFRAME PARA OBTENÇÃO DOS DADOS 

# In[4]:


import pandas as pd


# In[33]:


df = pd.read_csv("ocorrencia_2010_2020.csv", sep=";", parse_dates=['ocorrencia_dia'], dayfirst=True)
df


# In[6]:


df.loc[1, 'ocorrencia_cidade'] #extracao de dado da linha 1 e col. ocorrencia_cidade


# In[7]:


df.loc[4] #extracao de dados da linha com label (rotulo) 4


# In[8]:


df.loc[1:3] #extracao de dados das linhas com labels 1 até 3


# In[9]:


df.loc[[10, 40]] #extracao passando uma lista [] de linhas com labels 10 e 40


# In[10]:


df.loc[10, 40] #extracao da linha 10 e col. 40

#neste caso, ocorre erro pois não há col 40 no dataframe que tem apenas 9 col.


# In[11]:


df.loc[:,'ocorrencia_cidade'] #extracao de todos os dados da col ocorrencia_cidade


# In[12]:


df.codigo_ocorrencia.is_unique #label pode ser substituído por col. com valores unicos, que não se repetem

#cuidado para não confundir label ou índice do dataframe (de linhas e col.) com índice de array 


# In[13]:


df.ocorrencia_uf.is_unique #verificacao se UF tem dados únicos, para uso como indice do dataframe

#resultado indica que não é única


# In[14]:


df.set_index('codigo_ocorrencia') #transforma codigo_ocorrencia em indice do dataframe, ocupando a 1a. col. da esquerda

#mostra a visualização do dataframe com novo índice


# In[15]:


df.head(5) #verifica a troca de índices no dataframe

#percebe-se que não foram alterados as posição dos indices no arquivo


# In[16]:


df.set_index('codigo_ocorrencia', inplace=True) #alteracao dos indices é feita no dataframe com inplace=True


# In[17]:


df.head(5) #confirma se houve alteracao


# In[18]:


df.loc[40324] #extracao de dado pelo novo indice do dataframe

#novos indices podem ser usados como padrao de busca no dataframe


# In[19]:


df.reset_index(drop=True, inplace=True) #drop desfaz a alteracao de indice no dataframe local (inplace)


# In[20]:


df.head() #confirma a reversao para indices originais


# ### ALTERAÇÃO DOS DADOS

# In[21]:


df.loc[0, 'ocorrencia_aerodromo'] = '' #altera na linha 0 e col. aerodromo o dado **** por ''


# In[22]:


df.head(1) #verifica a alteracao somente na 1a. linha 


# In[23]:


df.loc[1] = 20 #altera todos os valores da linha 1 para valor 20


# In[24]:


df.head(2) #verifica alteracoes nas 2 primeiras linhas


# In[25]:


df.loc[:, 'total_recomendacoes'] = 10 #altera todos os dados (:) da col (total_recomendacoes) para 10

#exemplo didatico de alteracao total, porem nao é feito de fato porque há perda de dados, requer backup antes


# In[26]:


df #conferencia das alteracoes da coluna


# In[27]:


df['ocorrencia_uf_bkp'] = df.ocorrencia_uf #feito backup de uma coluna


# In[28]:


df #verifica inclusao da col do backup como ultima col do dataframe


# In[29]:


df.loc[df.ocorrencia_uf == 'SP', ['ocorrencia_classificacao']] = 'GRAVE' #alteracao com base em uma condicao

#filtro procura na col de ocorr_uf o dado SP e substitui dado da col ocorr_classificacao por GRAVE


# In[30]:


df.tail() #reimprime 5 ultimas linhas do dataframe para conferir alteracoes


# In[31]:


df.loc[df.ocorrencia_uf == 'SP'] #extrai todos os dados filtrados pela col SP


# In[34]:


#recarregar dataframe sem alteracoes para prosseguir com a limpeza
#rodar de novo as linhas de leitura do dataframe no começo do notebook
#df = pd.read_csv("ocorrencia_2010_2020.csv", sep=";", parse_dates=['ocorrencia_dia'], dayfirst=True)
#df.head(5)
df #reabertura do dataframe original


# ### LIMPEZA DOS DADOS
Levantamento de dados para limpeza por coluna conf. consulta em arquivo excel. 
Localizar todos que indicam dados não informados.
Resultado da pesquisa:
ocorrencia_uf
**
ocorrencia_aerodromo
###!
####
***
****
ocorrencia_hora
NULL
# In[145]:


#duplicar ultima linha do arquivo excel/csv, total = 5753 linhas 
#recarregar df depois de incluir linha no arq excel/csv para exemplificar funcao drop_duplicates

from IPython.display import Image #importa módulo IPython.display()do sub-pacote Imagem 
Image('dataframe_5753lines.jpg') #exibe imagem do dataframe com linhas duplicadas


# In[41]:


df.drop_duplicates() #funcao drop_duplicates localiza e exclui linhas duplicadas


# In[124]:


df.drop_duplicates(inplace=True) #exclusao definitiva de linhas duplicadas dentro do dataframe


# In[125]:


df #conferencia da exclusao

#excluir linha duplicadas dos arquivos excel/csv e rodar de novo o df


# In[42]:


df.loc[df.ocorrencia_aerodromo == '****', ['ocorrencia_aerodromo']] = pd.NA

#filtro na col ocorr_aerodromo e troca de **** por valor NA (padrao de substituicao)


# In[37]:


df.head() #verifica as substituicoes feitas <NA>


# In[43]:


df.replace(['**', '###!', '####', '***', '****', 'NULL'], pd.NA, inplace=True)

#funcao replace substui dados passados em lista [] por NA em todo dataframe


# In[44]:


df #conferencia das substituicoes


# In[45]:


df.isna() #funcao "isna" mostra onde ha dados nao informado com True


# In[46]:


df.isna().sum() #mostra soma de dados não informados em cada coluna


# In[47]:


df.isnull() #funcao "isnull" tambem mostra dados NA com True


# In[48]:


df.isnull().sum() #mesmo resultado de soma do isna().sum()


# In[49]:


df.fillna(0) #funcao "fillna" troca NA por valor 0 para visualizacao


# In[50]:


df.isnull().sum() #refaz a contagem de NA, permanece igual porque dataframe nao foi alterado pelo fillna


# In[51]:


df.fillna(10, inplace=True) #troca NA por 10 dentro do dataframe


# In[52]:


df.isnull().sum() #refaz a contagem apos alteracao do dataframe


# In[53]:


df.head(10) #verifica as trocas de NA por 10 nas primeiras 10 linhas


# In[54]:


df.replace([10], pd.NA, inplace=True) #substituicao definitiva de dado 10 por NA


# In[57]:


df.isnull().sum()

#resultado pode trazer mais dados do que na busca apos 1a troca por NA


# In[58]:


df.fillna(value={'total_recomendacoes': 10}, inplace=True)

#altera valor 10, passado em dicionario{}, por NA na col tot_recomendacoes 


# In[59]:


df.isnull().sum() #reexecuta contagem de NA


# In[60]:


df['total_recomendacoes_bkp'] = df.total_recomendacoes 

#refeito backup de coluna para demonstrar como excluir


# In[61]:


df.head() #verifica a insercao da nova col


# In[62]:


df.drop(['total_recomendacoes_bkp'], axis=1, inplace=True)

#exlusao definitiva da col passada em lista[] no dataframe 


# In[63]:


df.head() #confere a exclusao


# In[64]:


df.dropna() #exclusao de todas as linhas com NA no modo visualizacao - cuidado!!

#dataframe fica com linhas reduzidas de 5752 para 3552


# In[65]:


df #confere dataframe original 


# In[66]:


df.dropna(subset=['ocorrencia_uf']) #exclusao na visualizacao de linhas com NA no subconjunto ocorr_uf

#resultado demonstra perda de 1 linha do dataframe


# ###### Observações: dados não informados (NA = not avaliable) correspondem a Missing Values no contexto da Ciência
# de Dados, também tratado com o classificador NaN (not a number) com a biblioteca NumPy; datas recebem classificador
# NaT (not a time). Outro dado a ser tratado é o outlier, porque extrapola uma media ou, por exemplo, extrapola o
# número de recomendações para uma ocorrência no dataframe de acidentes aéreos. Em alguns casos o dado outlier é
# dropado (excluído) para possível transformação no futuro; podem ser adotadas soluções como excluir ou substituir.