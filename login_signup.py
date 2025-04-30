from pathlib import Path
import json

path = Path('user.json')


def login(users):
    CPF_ver = input('Bem vindo de volta, informe seu CPF: ')
    for user in users:
        if CPF_ver == user['CPF']:
            print(f"Bem vindo de volta, {user['nome_completo'].title()}")
                       
                            
def cadastro():
    if path.exists():
        brute_info = path.read_text()
        users = json.loads(brute_info)       
        usuario = {
                'nome_completo': input('Digite seu nome completo: '),
                'idade': input('Digite sua idade: '),
                'localizacao': input('Digite sua localizacao '),
                'CPF': input('Digite seu CPF: ')
            }

        users.append(usuario)
        content = json.dumps(users)
        path.write_text(content)
         
            
    else:    
        usuario = {
                'nome_completo': input('Digite seu nome completo: '),
                'idade': input('Digite sua idade: '),
                'localizacao': input('Digite sua localizacao '),
                'CPF': input('Digite seu CPF: ')
            }

        users = [usuario]
        content = json.dumps(users)
        path.write_text(content)    
        
    return users        
            


initial_ver = input('Você já possui uma conta? Digite SIM ou NAO: ').upper()
if initial_ver == 'NAO':
    cadastro()

if initial_ver == 'SIM':    
    info = path.read_text()
    users = json.loads(info)
    login(users)