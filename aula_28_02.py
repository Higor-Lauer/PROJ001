"""
Higor Rodrigues Lauer - 28-02-2024
SISTEMA DE DIRETÓRIOS
"""

import os
'''
root_dir = os.getcwd()
print(f'\nO path é: {root_dir}\n')
'''
'''
os.mkdir('clientes')
os.mkdir('produtos')
'''
'''
print(f'\nOs paths e arquivos são: {os.listdir(".")}\n')
'''
'''
root_dir = os.getcwd()
print(f'Diretório inicial do projeto: {root_dir}')

def directory_list(radix):
    for radix, directories, _ in os.walk(radix):
        if 'env' in directories:
            directories.remove('env')
        for directory in directories:
            print(f'Diretórios do projeto: {os.path.join(radix, directory)}')

directory_list(root_dir)
'''

'''
def build_tree(root_dir, prefix="", skip_dirs=None):
    if skip_dirs is None:
        skip_dirs = ['env', '.venv'] #Diretórios a se ignorar
    files = sorted(os.listdir(root_dir)) #Ordena arquivos e diretórios

    #filtra os arquivos para remover diretórios indesejados
    files_dirs = [f for f in files if os.path.isdir(os.path.join(root_dir, f)) and f not in skip_dirs]

    for i, filename in enumerate(files_dirs):
        path = os.path.join(root_dir, filename)
        is_last = 1 ==(len(files_dirs)-1)

        #mostra o diretório
        print((f"{prefix}{'|__' if is_last else '|--'}{filename}"))

        #se não for o último item adicione uma linha vertical embaixo
        extension = "   " if is_last else "|   "
        build_tree(path, prefix + extension, skip_dirs)

#obtém diretório atual e inicia a construção da árvore a partir dele
root_dir = os.getcwd()
print(f'Diretório inicial do projeto: {root_dir}')
build_tree(root_dir)
'''

'''
if 'clientes' in os.listdir():
    os.chdir('clientes')
    print(f'O path é: {os.getcwd()}\n')
else:
    print('A pasta clientes não foi encontrada no diretório atual.')
'''

'''
os.chdir('..')
print(f'\nO path é: {os.getcwd()}\n')
'''

'''
try:
    os.rename('clientes', 'cli')
    print(f'\nO novo nome é: {os.listdir(".")}\n')
except FileNotFoundError:
    print("O diretório ou arquivos 'clientes' não foi encontrado.")
'''

'''
os.rmdir('cli')
print(os.listdir('.'))
'''

'''
#define o diretório base e os subdiretórios
base_dir = 'proj001'
test_dir = os.path.join(base_dir, 'teste')
test_client_dir = os.path.join(test_dir, 'test_client')

#cria diretórios caso não existam
os.makedirs(test_client_dir, exist_ok=True)

#função para listar a estrutura de diretórios de forma recursiva 
def build_tree(root_dir, prefix=""):
    items = os.listdir(root_dir)
    items.sort()
    for i, item in enumerate(items):
        path = os.path.join(root_dir, item)
        is_last = 1 == (len(items) - 1)
        #checa se é um diretório e imprime de acordo
        if os.path.isdir(path):
            print(prefix + "|___" + item if is_last else prefix + "|---" + item)
            new_prefix = prefix + ("   " if is_last else "|   ")
            build_tree(path, new_prefix)
        else: #para arquivos
            print(prefix + "|___" + item if is_last else prefix + "|---" + item)

#imprime a estrutura a partir do diretório base
print(f'Estrutura de diretórios a partir de {base_dir}')
build_tree(base_dir)
'''

'''
#caminho base que será ajustado para o sistema operacional atual
base_path = os.path.join('Users', 'VITOR T.I', 'Documents', 'PROJ001', 'proj001', 'teste', 'test_client')

#verifica o sistema operacional e ajusta o caminho necessário
if os.name == 'nt':
    path_to_remove = os.path.join('C:\\', base_path)
else:
    path_to_remove = os.path.join('/', base_path)

try:
    os.rmdir(path_to_remove)
    print(f'O diretório {path_to_remove} foi removido com sucesso.')
except OSError as error:
    print(f'Erro ao remover o diretório{path_to_remove}: {error}')
'''