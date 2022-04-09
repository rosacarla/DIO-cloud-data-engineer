from datetime import date, time, datetime, timedelta

def trabalha_com_datetime(): #possivel acessar data e hora atual
    data_atual = datetime.now()
    print(data_atual) #mostra data, hora com milissegundos
    print(data_atual.strftime('%d/%m/%Y')) #mostra só data
    print(data_atual.strftime('%H:%M:%S')) #mostra só data
    print(data_atual.strftime('%d/%m/%Y %H:%M:%S')) #mostra data e hora sem milissegundos
    print(data_atual.strftime('%c')) #mostra data e hora apropriada da localidade
    print(data_atual.day)
    print(data_atual.year)
    print(data_atual.hour)
    print(data_atual.minute)
    print(data_atual.date())
    print(data_atual.weekday()) #hoje resultado 0 = Monday
    print(data_atual.month) #hoje resultado 3 = março
    tupla = ('seg', 'ter', 'qua', 'qui', 'sex', 'sab', 'dom')
    print(tupla[data_atual.weekday()])
    tupla = ('nul', 'jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez')
    print(tupla[data_atual.month])
    data_criada = datetime(2022, 3, 28, 18, 46, 22) #criacao de data
    print(data_criada)
    print(data_criada.strftime('%c'))
    data_string = '01/01/2022 12:20:22'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S') #conversao de datas
    print(data_convertida)
    print(type(data_convertida))
    nova_data = data_convertida - timedelta(days=365, hours=2, minutes=15, seconds=5) #subtracao com datas
    print(nova_data)
    nova_data = data_convertida + timedelta(days=365, hours=2, minutes=10, seconds=8) #adicao com datas
    print(nova_data)

def trabalha_com_date():
    data_atual = date.today()
    print(data_atual.strftime('%d/%m/%Y')) #pode por ou não "/", "-"; y minusculo para ano em 2 digitos
    data_atual_str = data_atual.strftime('%A %B %Y') #mostra dia semana, mês, ano
    print(type(data_atual))
    print(data_atual_str)
    print(type(data_atual_str))
#strftime em: https://docs.python.org/pt-br/3.7/library/datetime.html#strftime-and-strptime-behavior

def trabalha_com_time():
    horario = time(hour=15, minute=18, second=30)
    print(horario)
    print(type(horario))
    horario_str = horario.strftime('%H:%M:%S')
    print(horario_str)
    print(type(horario_str))

if __name__ == '__main__':
    #trabalha_com_date()
    #trabalha_com_time()
    trabalha_com_datetime()
