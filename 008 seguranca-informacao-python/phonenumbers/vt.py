import phonenumbers #importa lib de recursos para verificar telefones

from phonenumbers import geocoder #importa metodo geocoder para trazer localizacao

phone = input('Digite o telefone no formato +551140028922: ') #recebe telefone para consulta

phone_number = phonenumbers.parse(phone) #phone pode ser de celular

print(geocoder.description_for_number(phone_number, 'pt')) #imprime descricao do telefone em portugues