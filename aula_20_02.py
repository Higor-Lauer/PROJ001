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
    return print("\nA lâmpada é do tipo: ", self.tipo), print('Voltagem: ',self.voltagem,' volts'), print('Cor: ',self.cor), print('Lumens: ',self.lumens), print('A lâmpada está ', self.status)

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