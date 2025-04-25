from pathlib import Path
import json

path = Path('user.json')


def login(data):
    if path.exists():
        info = json.loads(data)
        ver_login = input('Bem vindo de volta! Informe seu CPF: ')
        if ver_login == info['CPF']:
            print(f"Bem vindo de volta, {info['nome_completo']}")
                            
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

initial_ver = input('Você já possui uma conta? Digite SIM ou NAO: ')
if initial_ver == 'NAO':
    cadastro()

if initial_ver == 'SIM':    
    data = path.read_text()
    login(data)   
    
    







