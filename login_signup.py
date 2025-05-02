from pathlib import Path
import json

path = Path('user.json')

##verifica cada dicionario em busca do CPF correspondente e da boas vindas ao nome do mesmo
def login(users):
    CPF_ver = input('Bem vindo de volta, informe seu CPF: ')
    for database in users:
        for CPF in database:
            if CPF == CPF_ver:
                print(f'Bem vindo, {database[CPF]["nome_completo"]}!')
                      
##caso não exista dicionario cadastrado, o input é feito e criado uma lista onde o dicionario é convertido e armazenado em JSON.                          
##caso exista dicionario cadastrado, o input é feito da mesma forma, mas o dicionario capturado é adicionado a lista existente, e logo convertida e armazenada em JSON.
def cadastro():
    if path.exists():
        brute_info = path.read_text()
        users = json.loads(brute_info)     
        CPF = input('Qual seu CPF?: ')
        usuario = {
                'nome_completo': input('Digite seu nome completo: '),
                'idade': input('Digite sua idade: '),
                'localizacao': input('Digite sua localizacao '),
                'saldo': 0
            }
        database = {CPF: usuario}
        users.append(database)
        content = json.dumps(users)
        path.write_text(content)
         
    ## ESQUEMA DE ARMAZENAMENTO: a lista USERS, armazena o dicionario DATABASE, cuja chave é CPF, cuja armazena o dicionario USUARIO que contem as informações.                
    
    else:    
        CPF = input('Qual seu CPF?: ')
        usuario = {
                'nome_completo': input('Digite seu nome completo: '),
                'idade': input('Digite sua idade: '),
                'localizacao': input('Digite sua localização: '),
                'saldo': 0
            }

        database = {CPF: usuario}
        users = [database]
        content = json.dumps(users)
        path.write_text(content)    
        
    return users        
            
initial_ver = input('Você já possui uma conta? Digite SIM ou NAO: ').upper() #INICIO DO CÓDIGO
if initial_ver == 'NAO':
    cadastro()

if initial_ver == 'SIM':    
    info = path.read_text() #CAPTURA AS INFORMAÇÕES
    users = json.loads(info)
    login(users)

