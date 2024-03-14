"""
Higor Rodrigues Lauer - 13-03-2024
PARADIGMAS DE ORIENTAÇÃO AO OBJETO
"""

import time 

'''
class Televisao:
    def __init__(self, marca, modelo, tamanho_tela, tipo_tecnologia, voltagem, nr_series, codigo_barras, preco):
        self.marca = marca
        self.modelo = modelo
        self.tamanho_tela = tamanho_tela
        self.tipo_tecnologia = tipo_tecnologia
        self.voltagem = voltagem
        self.nr_series = nr_series
        self.codigo_barras = codigo_barras
        self.preco = preco 
        self.ligada = False
        self.conectada = False
        self.canais = 1

    def verifica_tv_ligada(self):
        return self.ligada
    
    def ligar_desligar(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True
    
    def verifica_conexao(self):
        return self.conectada
    
    def conecta_tv(self):
        if self.conectada:
            self.conectada = False
        else:
            self.conectada = True

print()
print('>>>Dados da televisão<<<')
print()

marca           = input('Marca...........................................:')
modelo          = input('Modelo..........................................:')
tamanho_tela    = input('Tamanho da tela em poleogadas...................:')
tipo_tecnologia = input('Tipo de tecnologia..............................:')
voltagem        = input('Voltagem........................................:')
nr_series       = input('Número de série.................................:')
codigo_barras   = input('Código de barras................................:')
preco           = input('Preço de venda R$...............................:')

tv_1 = Televisao(marca, modelo, tamanho_tela, tipo_tecnologia, voltagem, nr_series, codigo_barras, preco)

print()
print(f'A TV: {tv_1.marca} - {tv_1.tipo_tecnologia} - {tv_1.modelo} - está ligada? {tv_1.verifica_tv_ligada()}')
print()
print('Aguarde enquanto sua tv é ligada!!!')
time.sleep(1)
tv_1.ligar_desligar()
print()
print('      - Utilizando sua televisão-')
print()
print(f'>>> Bem-vindo à sua televisão: {tv_1.marca} - {tv_1.tipo_tecnologia} - modelo: {tv_1.modelo} <<<')
print(f'      - Você está no menu principal do cliente - canal: {tv_1.canais}')
print()
print(input('>>> Escolha uma opção para aproveitar tudo que nossa tecnologia tem a oferecer <<<'))
print()
'''
'''
class Lampada:
    def __init__(self,cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False
    
    def checa_lampada(self):
        return self.__ligada
    
    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True

lampada_1 = Lampada('Amarela', 220, 1200)

print(f'A lampada está ligada? {lampada_1.checa_lampada()}')

lampada_1.ligar_desligar()

print(f'A lampada está ligada? {lampada_1.checa_lampada()}')
'''
'''
class Cliente:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

class ContaCorrente:
    contador = 4999

    def __init__(self, limite, saldo, cliente):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero

    def mostra_cliente(self):
        print(f'\nO cliente é: {self.__cliente._Cliente__nome}')
    
    def mostra_saldo(self):
        print(f'\nO cliente é: {self.__cliente._Cliente__nome} possui um saldo total (saldo+limite) de: {self.__saldo + self.__limite}')

cliente_1 = Cliente('Gertrudez', '123.123.123-80')
conta = ContaCorrente(2565, 4500, cliente_1)

conta.mostra_cliente()

conta.mostra_saldo()
'''