from pathlib import Path
import json ##importacao das bibliotecas

path = Path('user.json') ##definindo path do json

##login com uma mensagem de boas vindas
def login(data):
    if path.exists():
        info = json.loads(data)
        ver_login = input('Bem vindo de volta! Informe seu CPF: ')
        if ver_login == info['CPF']:
            print(f"Bem vindo de volta, {info['nome_completo']}")

#cadastro e armazenamento de informações                            
def cadastro():
    usuario = {
        'nome_completo': input('Digite seu nome completo: '),
        'idade': input('Digite sua idade: '),
        'localizacao': input('Digite sua localizacao '),
        'CPF': input('Digite seu CPF: ')
    }

    data = json.dumps(usuario)
    path.write_text(data)
    print('Seu cadastro foi concluido')
    return data

##verificação para cadastrar ou logar-se

initial_ver = input('Você já possui uma conta? Digite SIM ou NAO: ')
if initial_ver == 'NAO': ##redireciona para criar uma conta
    cadastro()

if initial_ver == 'SIM': ##captura as informações e redireciona para login    
    data = path.read_text()
    login(data)   
    
    







