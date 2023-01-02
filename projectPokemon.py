import random
import time

repetir = True

def sleep(x):
    time.sleep(x)

class Pokemon:
    def __init__(self, species, hp, atk):
        self.species = species
        self.hp = hp
        self.atk = atk

class Grass(Pokemon):
    def __init__(self, species, hp, atk):
        super().__init__(species, hp, atk)
        
class Water(Pokemon):
    def __init__(self, species, hp, atk):
        super().__init__(species, hp, atk)
        
class Fire(Pokemon):
    def __init__(self, species, hp, atk):
        super().__init__(species, hp, atk)
        
class Electric(Pokemon):
    def __init__(self, species, hp, atk):
        super().__init__(species, hp, atk)
        
class Trainer:
    def __init__(self, name, pokemons):
        self.name = name
        self.pokemons = pokemons
        
class Player(Trainer):
    def __init__(self, name, pokemons, money, pokeballs):
        super().__init__(name, pokemons)
        self.money = money
        self.pokeballs = pokeballs
        
class Rival(Trainer):
    def __init__(self, name, pokemons):
        super().__init__(name, pokemons)

Bulbasaur = Grass("Bulbasaur", 30, 10)
Squirtle = Water("Squirtle", 40, 10)
Charmander = Fire("Charmander", 30, 15)
Pikachu = Electric("Pikachu", 35, 10)

listaPokemons = [Bulbasaur, Squirtle, Charmander, Pikachu]
pokemonsCapturados = []

def menu():
    print("\n\nVocê está no menu.")
    repetir = True
    while(repetir):
        sleep(1)
        acao = input("\n\nO que fazer?\n\n1- Capturar um Pokémon\n2- Batalhar\n3- Suas informações\n\n")
        if acao == "1":
            pokeCatch(jogador, poke="")
        elif acao == "2":
            pokeBattle(jogador, rival, poke1="", poke2="")
        elif acao == "3":
            playerInfo(jogador)
        else:
            print("\n\nAção inválida, tente novamente.")
            repetir = True

def pokeCatch(self, poke):
    repetir = True
    poke = random.choice(listaPokemons)
    print(f"\n\nVocê encontrou um {poke.species}!")
    sleep(1)
    while(repetir):
        repetir = False
        if self.pokeballs > 0:
            acao = input(f"\n\nO que fazer?\n\n1- Jogar Pokébola ({self.pokeballs} restantes)\n2- Fugir\n\n")
            if acao == "1":
                print("\n\nVocê jogou uma Pokébola!")
                self.pokeballs -= 1
                sleep(1)
                print("\n\n...")
                sleep(2)
                chancesCaptura = [1, 2]
                capturou = random.choice(chancesCaptura)
                if capturou == 1:
                    print(f"\n\nVocê capturou o Pokémon {poke.species}!")
                    self.pokemons += 1
                    pokemonsCapturados.append(poke)
                else:
                    print("\n\nO Pokémon escapou da Pokébola!")
                    repetir = True
            if acao == "2":
                sleep(1)
                print("\n\nVocê fugiu.")
        else:
            print("\n\nVocê está sem Pokébolas! O Pokémon escapou para a floresta.")
            
def pokeBattle(self, rival, poke1, poke2):
    print(f"\n\nVocê encontrou seu rival {rival.name}!")
    acao = input("\n\nO que fazer?\n\n1- Batalhar\n2- Fugir\n\n")
    if acao == "1":
        poke2 = random.choice(listaPokemons)
        print(f"\n\nO rival utilizará o Pokémon {poke2.species} para a batalha.")
        seupoke = input("\n\nQual Pokémon você utilizará?\n")
    elif acao == "2":
        print("\n\nVocê fugiu.")
        
def playerPokemons():
    for p in pokemonsCapturados:   
        print(p.species)
def playerInfo(self):
    print(f"\n\nNome: {self.name}\nDinheiro: ¥{self.money}\nPokébolas: {self.pokeballs}\nPokémons ({self.pokemons})\n\n{playerPokemons}")

jogador = Player(input("\n\nQual o seu nome? "), 0, 500, 5)
nomesRival = ["Tarik", "Gary", "Chiquin", "James", "Tonho"]
rival = Rival(random.choice(nomesRival), 0)
sleep(1)
print(f"\n\nOlá {jogador.name}. Sua jornada começará agora.")
sleep(1)
print("\n\nPrimeiro, vamos escolher um Pokémon inicial.\n\nEscolha entre os 3 Pokémons:")
while(repetir):
    repetir = False
    sleep(1)
    inicial = input("\n1- Bulbasaur\n2- Squirtle\n3- Charmander\n\n")
    if inicial == "1":
        pokemonsCapturados.append(Bulbasaur)
        jogador.pokemons += 1
    elif inicial == "2":
        pokemonsCapturados.append(Squirtle)
        jogador.pokemons += 1
    elif inicial == "3":
        pokemonsCapturados.append(Charmander)
        jogador.pokemons += 1
    else:
        print("\n\nAlgo deu errado, tente novamente.")
        repetir = True
        
print(f"\n\nVocê escolheu o Pokémon {pokemonsCapturados[0].species} como seu inicial.")

menu()