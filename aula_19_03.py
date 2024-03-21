"""
Higor Rodrigues Lauer - UTF-8 - pt-br - 13-03-2024
aula_13_03.py
"""

'''
class Animal:
    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def som(self, som):
        print(f'O som que o {self.__nome} faz chama-se: {som}')

class Elefante(Animal):
    def __init__(self, nome, especie, raca):
        super().__init__(nome, especie)
        super().som('Bramido')
        self.__raca = raca

class Girafa(Animal):
    def __init__(self, nome, especie, raca):
        super().__init__(nome, especie)
        self.__raca = raca

dumbo = Elefante('Elefante', 'Africano', 'Loxodonta Africana')

gisela = Girafa('Girafa', 'Africana', 'Giraffidae')

gisela.som('Zumbido')
'''
'''
#Multideriveção direta

class SuperClasse_1:
    pass

class SuperClasse_2:
    pass

class SuperClasse_3:
    pass

class Multi_Derivada_Direta(SuperClasse_1, SuperClasse_2, SuperClasse_3):
    pass
'''
'''
#Multiderivação indireta
class SuperClasse_1:
    pass

class SuperClasse_2(SuperClasse_1):
    pass

class SuperClasse_3(SuperClasse_2):
    pass

class Multi_Derivada_Indireta(SuperClasse_3):
    pass
'''
'''
class Animal:

    def __init__(self, nome):
        self.__nome= nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'
    
class Terrestre(Animal): # Herança direta
    def __init__(self, nome):
        super().__init__(nome)
    
    def andar(self):
        return f'Olá eu sou {self._Animal__nome} e estou andando pela mata'
    
    def cumprimentar(self): #sobrescrição do método da classe super()
        return f'Eu sou {self._Animal__nome} e vivo em florestas tropicais!'
    
tatu = Terrestre('Tatu bola') #herança direta
print()
print(tatu.andar())
print()
print(tatu.cumprimentar())

# Analisando qual instância pertence ao tatu:

print(f'\nTatu Bola é instância de Terrestre? {isinstance(tatu, Terrestre)}')

class Aquatico(Animal): # Herança direta
    def __init__(self, nome):
        super().__init__(nome)
    
    def nadar(self):
        return f'O {self._Animal__nome} nada e é um peixe filtrante.'
    
    def cumprimentar(self): #sobrescrição do método da classe super()
        return f'Eu sou {self._Animal__nome} e vivo em água doce!'
    
peixe = Aquatico('Tambaqui') #herança direta
print()
print(peixe.nadar())
print()
print(peixe.cumprimentar())

# Analisando qual instância pertence ao tatu:

print(f'\nTambaqui é instância de Aquatico? {isinstance(peixe, Aquatico)}')
'''
'''
class Animal:

    def __init__(self, nome):
        self.__nome = nome
    
    def cumprimentar(self):
        return f'Eu sou {self.__nome}'
    
class Terrestre(Animal): # Herança direta
    def __init__(self, nome):
        super().__init__(nome)
    
    def andar(self):
        return f'Olá eu sou {self._Animal__nome} e estou andando pela mata'
    
    def cumprimentar(self): #sobrescrição do método da classe super()
        return f'Eu sou {self._Animal__nome} e vivo em florestas tropicais!'
    
class Aquatico(Animal): # Herança direta
    def __init__(self, nome):
        super().__init__(nome)
    
    def nadar(self):
        return f'O {self._Animal__nome} nada e é um peixe filtrante.'
    
    def cumprimentar(self): #sobrescrição do método da classe super()
        return f'Eu sou {self._Animal__nome} e vivo em água doce!'
'''
'''  
class Ornintorrinco(Terrestre, Aquatico): #classe multivalorada direta

    def __init__(self, nome):
        super().__init__(nome)

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} e vivo na terra e na água doce!'
    
perry = Ornintorrinco('Perry')

print('\n', perry.andar())
print('\n', perry.nadar())
print('\n', perry.cumprimentar())


class Pinguim(Ornintorrinco):#Classe multiderivada indireta
    def __init__(self, nome):
        super().__init__(nome)
    
    def cumprimentar(self):#sobrescrição do método da classe super()
        return f'Eu sou {self._Animal__nome} e vivo na terra e na água salgada!'
    
pinguim = Pinguim('Picolino')
print()
print(pinguim.nadar())
print()
print(pinguim.cumprimentar())

#analisando a que instância pinguim pertence
print()
print(f'Pinguim Picolino é da instância ornintorrinco? {isinstance(pinguim, Ornintorrinco)}')
'''
'''
class Ornintorrinco(Terrestre, Aquatico): #classe multivalorada direta

    def __init__(self, nome):
        super().__init__(nome)

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} e vivo na terra e na água doce!'

perry = Ornintorrinco('Perry')    
print('\n', perry.cumprimentar())
print(help(Ornintorrinco))
'''
'''
class Animal(object):

    def __init__(self, nome):
        self.__nome = nome
    
    def emite_som(self):
        raise NotImplementedError('A classe filha precisa implementar esse método')
    
    def come(self):
        print(f'{self.__nome} está comendo')

class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)
    
    def emite_som(self):
        print(f'{self._Animal__nome} fala BABY IM GONNA PREY ON YOU TONIGHT')

class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)
    
    def emite_som(self):
        print(f'{self._Animal__nome} fala miau')

print()
feliz = Gato('Feliz')
feliz.come()
feliz.emite_som()

print()
gerivaldo = Cachorro('Gerivaldo')
gerivaldo.come()
gerivaldo.emite_som()
'''
'''
class Livros:
    def __init__(self, titulo, autor, paginas):
        self.__titulo = titulo
        self.__autor = autor
        self.__paginas = paginas
    
    def __repr__(self):
        return f'{self.__titulo} escrito por {self.__autor}'

livro_1 = Livros('Python: Muito texto', 'Rafael Lanches', 225)
livro_2 = Livros('Branca de Neve', 'Robson', 12)

print(f'\nLivro: {livro_1}')
print(f'\nLivro: {livro_2}')
'''
'''
class Livros:
    def __init__(self, titulo, autor, paginas):
        self.__titulo = titulo
        self.__autor = autor
        self.__paginas = paginas
    
    def __str__(self):
        return f'{self.__titulo} escrito por {self.__autor} - nº páginas: {self.__paginas}'

livro_1 = Livros('Python: Muito texto', 'Rafael Lanches', 225)
livro_2 = Livros('Branca de Neve', 'Robson', 12)

print(f'\nLivro: {livro_1}')
print(f'\nLivro: {livro_2}')
'''