import random
import time
import pokemonTrainers

# 1. Modelar Classe Pokemon
class Pokemon:
    def __init__(self, species, hp, maxhp, atk):
        self.species = species
        self.hp = hp
        self.maxhp = maxhp
        self.atk = atk

# 2. Modelar pelo menos 3 subclasses de Pokemon com base no seu tipo
class Grass(Pokemon):
    def __init__(self, species, hp, maxhp, atk):
        super().__init__(species, hp, maxhp, atk)
        
class Water(Pokemon):
    def __init__(self, species, hp, maxhp, atk):
        super().__init__(species, hp, maxhp, atk)
        
class Fire(Pokemon):
    def __init__(self, species, hp, maxhp, atk):
        super().__init__(species, hp, maxhp, atk)
        
class Electric(Pokemon):
    def __init__(self, species, hp, maxhp, atk):
        super().__init__(species, hp, maxhp, atk)

Bulbasaur = Grass("Bulbasaur", 30, 30, 10)
Squirtle = Water("Squirtle", 40, 40, 10)
Charmander = Fire("Charmander", 30, 30, 15)
Pikachu = Electric("Pikachu", 35, 35, 10)

listaPokemons = [Bulbasaur, Squirtle, Charmander, Pikachu]
pokemonsCapturados = []
        