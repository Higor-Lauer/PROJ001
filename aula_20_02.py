"""
Higor Rodrigues Lauer - 20-02-2024
PARADIGMA DA ORIENTAÇÃO A OBJETOS
"""

#Orientação ao objeto
#Criando classe:
'''
class Animal:
    def __init__(self, tipo, tamanho = None, peso = None, idade= None):
        self.tipo = tipo
        self.tamanho = tamanho
        self.peso = peso
        self.idade = idade

#Definindo método comer da classe Animal
        
def comer(self):
    return print('O ', self.tipo,' está comendo!')

# Criando o objeto elefante da classe animal e passando seus argumentos

elefante = Animal('Elefante',3,2700,30)

#Apresentando em tela os atributos do objeto elefante recebidos da classe Animal

print('\nTipo do animal', elefante.tipo)
print('Tamanho: ',elefante.tamanho,' metros de altura')
print('Peso: ',elefante.peso,' quilos')
print('Idade: ',elefante.idade,' anos')
print(f'Ele é da classe {type(elefante)}')
'''

#Exercício
'''
class Lampadas:
    def __init__(self, tipo, voltagem = None, cor = None, lumens = None, status = None):
        self.tipo = tipo
        self.voltagem = voltagem
        self.cor = cor
        self.lumens = lumens
        self.status = status

lampada_sl = Lampadas('Fluorescente', 110, 'Branca', 1200, 'Ligada')
lampada_qt = Lampadas('Incandescente', 110, 'Amarela', 900, 'Desligada')
lampada_cz = Lampadas('LED', 220, 'Azul', 2400, 'Ligada')

def estado_lampada(self):
    print("\nA lâmpada é do tipo: ", self.tipo), 
    print('Voltagem: ',self.voltagem,' volts'), 
    print('Cor: ',self.cor), 
    print('Lumens: ',self.lumens), 
    print('A lâmpada está ', self.status)

estado_lampada(lampada_sl)
estado_lampada(lampada_qt)
estado_lampada(lampada_cz)
'''

'''
class ContaCorrente:
    def __init__(self, nome, agência, valor):
        self.nome = nome
        self.agência = agência
        self.valor = valor
class Produto:
    def __init__(self, nome, codigo, preco):
        self.nome = nome
        self.codigo = codigo
        self.preco = preco
class Usuario:
    def __init__(self, nome, senha, idade, id):
        self.nome = nome
        self.senha = senha
        self.idade = idade
        self.id = id
'''

#Definindo atributos de instância privados de uma classe
'''
class LoginIntranet:
    def __init__(self, email, senha):
        self.__email = email
        self.__senha = senha

usuario = LoginIntranet('teste@gmail.com', '123456')

#print(usuario.__senha)
#print(usuario.__email)

#print(dir(usuario))

print(f'\nO e-mail do usuário é: {usuario._LoginIntranet__email}')
print(f'A senha do usuário é: {usuario._LoginIntranet__senha}\n')
'''

#Definindo uma classe e métodos para acessar seus atributos de instância público ou privado de fora da classe
'''
class LoginIntranetDois:
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_email(self):
        print(self.email)
    
    def mostra_senha(self):
        print(self.__senha)

usuario_dois = LoginIntranetDois('two@gmail.com', 'senhabraba2')

usuario_dois.mostra_email()

usuario_dois.mostra_senha()

usuario_tres = LoginIntranetDois('three@gmail.com', 'senhabraba3')

usuario_quatro = LoginIntranetDois('four@gmail.com', 'senhabraba4')

usuario_cinco = LoginIntranetDois('five@gmail.com', 'senhabraba5')

usuario_seis = LoginIntranetDois('six@gmail.com', 'senhabraba6')

usuario_tres.mostra_email()
usuario_tres.mostra_senha()

usuario_quatro.mostra_email()
usuario_quatro.mostra_senha()

usuario_cinco.mostra_email()
usuario_cinco.mostra_senha()

usuario_seis.mostra_email()
usuario_seis.mostra_senha()
'''

'''
class Produto:
    imposto = 1.08

    def __init__(self, descricao, cor, marca, tela, valor):
        self.descricao = descricao
        self.cor = cor
        self.marca = marca
        self.tela = tela
        self.valor = (valor * Produto.imposto)

    def mostra_na_tela(self):
        print(self.descricao)
        print(self.cor)
        print(self.marca)
        print(self.tela)
        print(self.valor)

produto1 = Produto('Notebook Gamer', 'Preto', 'Dell', 'Monitor 15', 13542.25)
produto2 = Produto('Magic Mouse 2 A1657', 'Branco', 'Apple', '2,16 X 5,71 cm', 675.00)

produto1.mostra_na_tela()
print()
produto2.mostra_na_tela()
'''

'''
class Produto:
    imposto = 1.12
    contador = 0

    def __init__(self, descricao, cor, marca, tela, valor):
        self.id = Produto.contador + 1
        self.descricao = descricao
        self.cor = cor
        self.marca = marca
        self.tela = tela
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id

    def mostra_na_tela(self):
        print(self.id)
        print(self.descricao)
        print(self.cor)
        print(self.marca)
        print(self.tela)
        print(self.valor)

produto1 = Produto('Notebook Gamer', 'Preto', 'Dell', 'Monitor 15', 13542.25)
produto2 = Produto('Magic Mouse 2 A1657', 'Branco', 'Apple', '2,16 X 5,71 cm', 675.00)
produto1.peso = '5 Kg'
produto2.peso = '900 gr'

produto1.mostra_na_tela()
print(f'Peso: {produto1.peso}')
print()
produto2.mostra_na_tela()
print(f'Peso: {produto2.peso}')

print('\n',dir(produto1))
print('\n',dir(produto2))

del produto2.tela
del produto2.peso

print('\n',dir(produto2))
'''