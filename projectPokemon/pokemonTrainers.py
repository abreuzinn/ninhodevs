import random

# 3. Modelar Classe Treinador. Essa classe deve conter como atributo uma lista de Pokemons.       
class Trainer:
    def __init__(self, name="", pokemons=[]):
        self.name = name
        self.pokemons = pokemons

# 4. Modelar subclasses de Treinador: Jogador e Inimigo
class Player(Trainer):
    def __init__(self, name="", pokemons=[], money="", pokeballs=""):
        super().__init__(name, pokemons)
        self.money = money
        self.pokeballs = pokeballs
        
class Rival(Trainer):
    def __init__(self, name="", pokemons=[]):
        super().__init__(name, pokemons)

nomesRival = ["Tarik", "Gary", "Chiquin", "James", "Tonho"]
rival = Rival(random.choice(nomesRival), 0)