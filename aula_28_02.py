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