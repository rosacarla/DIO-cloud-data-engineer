#!/usr/bin/env python
# coding: utf-8

# # **PROJETO: ANÁLISE DE ACIDENTES AÉREOS DO CENIPA**
# ### Autora: Carla Edila Silveira
# ### Base: Opendata AIG Brazil - acidentes aéreos do CENIPA

# ### ETAPA DE EXTRAÇÃO DE DADOS

# In[1]:


import pandas as pd #importa bilbioteca Pandas

#apelido mais usual eh "pd"


# In[9]:


#pip install pandera ##instala a biblioteca Pandera
#apos instalacao Jupyter informa que deve ser reiniciado o Kernel (pelo botao atualizar)
#apos reiniciar kernel, transformar em texto a linha do pip para não repetir esses passos 


# In[3]:


import pandera as pa #importa biblioteca para montar esquema de validacao do dataframe


# In[16]:


df = pd.read_csv("ocorrencia_2010_2020.csv", sep=";", parse_dates=['ocorrencia_dia'], dayfirst=True)
#nome do arq.csv(sem caminho)por estar na pasta do projeto
#metodo read_csv retorna um objeto de dados - dataframe susbtituído por "df" como usual na comunidade
#parse_dates indica quais colunas serao convertidas em data, informadas em uma lista []
#dayfirst fixa que o dia vem primeiro que o mês, pois estavam invertidos na extração inicial 

df.head(10) #imprime primeiras 10 linhas do dataframe 

#arq csv = arq separado por virgula; separador de colunas (ponto e virgula) passado por parametro acima 
#1a. visualizacao imprimiu 5 linhas iniciais e finais do arquivo
#pode usar "tail" para conferir as 10 ultimas linhas
#em campos vazios (sem dado informado), pode vir "NaT" pra data, "NaN" pra texto, a tratar na limpeza


# In[33]:


df.dtypes #exibe os tipos de dados do dataframe

#na 1a. extração observa-se que coluna de datas consta o tipo objeto
#apos conversao, visualiza-se a coluna reconhecida como datetime
#conversao do parse pode falhar se houver data fora do padrao de data/calendario.
#por ex, uma data inadequada como "03/50/2020" impede a conversao, col permanece como obj.


# In[34]:


df.ocorrencia_dia #extracao somente da coluna de datas


# In[35]:


df.ocorrencia_dia.dt.month #extração de mês da data

#1a. extração falha porque coluna data foi carregada como: "ocorrencia_dia object"
#AttributeError: Can only use .dt accessor with datetimelike values
#coluna de datas requer outra conversão para facilitar extrações de dia, mês, ano
#apos conversao, 2a. extracao exibe os meses das datas


# ###### Obs.: Dataframe carregado na memória do servidor com primeiras conversoes necessarias.

# ### ETAPA DE VALIDAÇÃO DOS DADOS

# In[31]:


#bloco do esquema completo de validacao dos dados
#parametros das colunas devem ser compativeis com tipo de dados pra rodar a validacao (conferir pelo dtypes)
schema = pa.DataFrameSchema(  
    columns = {        
        "codigo":pa.Column(pa.Int, required=False),
        "codigo_ocorrencia":pa.Column(pa.Int), 
        "codigo_ocorrencia2":pa.Column(pa.Int),
        "ocorrencia_classificacao":pa.Column(pa.String),
        "ocorrencia_cidade":pa.Column(pa.String),
        "ocorrencia_uf":pa.Column(pa.String,pa.Check.str_length(2,2)),
        "ocorrencia_aerodromo":pa.Column(pa.String),
        "ocorrencia_dia":pa.Column(pa.DateTime),
        "ocorrencia_hora":pa.Column(pa.String,pa.Check.str_matches(r'^([0-1]?[0-9]|[2][0-3]):([0-5][0-9])(:[0-5][0-9])?$'),
                                    nullable=True),
        "total_recomendacoes":pa.Column(pa.Int)                                               
    }
)


# In[32]:


schema.validate(df) #executa a validacao

#1a validacao: visualizacao confirma que dataframe foi validado pela col codigo_ocorrencia que tem nros int.
#2a. validacao: falha por erro na coluna de hora, como segue:
#SchemaError: non-nullable series 'ocorrencia_hora' contains null values:
#4100    NaN
#Name: ocorrencia_hora, dtype: object
#3a. validacao: dataframe foi validado mediante o esquema proposto
#4a. validacao: inserida função Check de restrição com expressao regular para formatar hora em 24hs
#5a. validacao: inserida fç Check com restrição de tamanho min/max da UF que será com 2 letras
#6a. validacao: inserida col "codigo" no schema pra verificar se há essa col no df; saída do erro abaixo
#SchemaError: column 'codigo' not in dataframe; incluiu-se parametro required(False), habitual eh True
#7a. validacao: concluída etapa de validacao do dataframe