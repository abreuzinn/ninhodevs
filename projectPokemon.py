import random
import time

repetir = True

def sleep(x):
    time.sleep(x)

class Pokemon:
    def __init__(self, species, hp, maxhp, atk):
        self.species = species
        self.hp = hp
        self.maxhp = maxhp
        self.atk = atk

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

Bulbasaur = Grass("Bulbasaur", 30, 30, 10)
Squirtle = Water("Squirtle", 40, 40, 10)
Charmander = Fire("Charmander", 30, 30, 15)
Pikachu = Electric("Pikachu", 35, 35, 10)

listaPokemons = [Bulbasaur, Squirtle, Charmander, Pikachu]
pokemonsCapturados = []

def menu():
    def endCode():
        sleep(1)
        print("\n\nPrograma encerrado.")
    print("\n\nVocê está no menu.")
    repetir = True
    while(repetir):
        sleep(1)
        acao = input("\n\nO que fazer?\n\n1- Capturar um Pokémon\n2- Batalhar\n3- Suas informações\n4- Ir ao Centro Pokémon\n5- Ir para a Loja\n0- Encerrar programa\n\n")
        if acao == "1":
            if jogador.pokemons == 6:
                print("Você está com sua party cheia. Exclua algum de seus Pokémons.")
            else:
                pokeCatch(jogador, poke="")
        elif acao == "2":
            pokeBattle(jogador, rival, poke1="", poke2="")
        elif acao == "3":
            playerInfo(jogador)
        elif acao == "4":
            pokeCenter()
        elif acao == "5":
            pokeShop(jogador)
        elif acao == "0":
            endCode()
            break
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
    sleep(1)
    acao = input("\n\nO que fazer?\n\n1- Batalhar\n2- Fugir\n\n")
    sleep(1)
    if acao == "1":
        poke2 = random.choice(listaPokemons)
        print(f"\n\nO rival utilizará o Pokémon {poke2.species} para a batalha.")
        sleep(1)
        repetir = True
        while(repetir):
            repetir = False
            try:
                print(f"\n\nQual Pokémon você utilizará?\n")
                sleep(1)
                {playerPokemons()}
                print("0- Fugir")
                seupoke = input("\n\n")
                if seupoke == "1":
                    poke1 = pokemonsCapturados[0]
                elif seupoke == "2":
                    poke1 = pokemonsCapturados[1]
                elif seupoke == "3":
                    poke1 = pokemonsCapturados[2]
                elif seupoke == "4":
                    poke1 = pokemonsCapturados[3]
                elif seupoke == "5":
                    poke1 = pokemonsCapturados[4]
                elif seupoke == "6":
                    poke1 = pokemonsCapturados[5]
                elif seupoke == "0":
                    print("Você fugiu.")
                    break
                else:
                    print("Escolha um de seus Pokémons! Tente novamente.")
                    repetir = True
                if poke1.hp <= 0:
                    print("\n\nO Pokémon escolhido está desmaiado. Escolha outro.")
                    repetir = True
            except:
                IndexError(print("Você não possui este Pokémon."))
                repetir = True
            while (poke1.hp > 0) or (poke2.hp > 0):
                sleep(1)
                acao = input("\n\nO que fazer?\n\n1- Atacar\n2- Fugir\n\n")
                if acao == "1":
                    sleep(1)
                    print(f"\n\n{poke1.species} atacou {poke2.species}!")
                    poke2.hp -= poke1.atk
                    print(f"Dano: {poke1.atk}\nHP restante de {poke2.species}: {poke2.hp}/{poke2.maxhp}")
                    if poke2.hp <= 0:
                        poke2.hp = 0
                        break
                    else:
                        sleep(1)
                        print(f"\n\n{poke2.species} atacou {poke1.species}!")
                        poke1.hp -= poke1.atk
                        print(f"Dano: {poke2.atk}\nHP restante de {poke1.species}: {poke1.hp}/{poke1.maxhp}")
                    if poke1.hp <= 0:
                        poke1.hp = 0
                        break
            if poke1.hp == 0:
                sleep(1)
                print("\nVocê perdeu.")
            elif poke2.hp == 0:
                sleep(1)
                print("\nVocê ganhou!")
                sleep(1)
                granarecebida = random.randint(50, 100)
                print(f"\nVocê recebeu ¥{granarecebida}.")
                jogador.money += granarecebida
    elif acao == "2":
        print("\n\nVocê fugiu.")
        
def playerInfo(self):
    print(f"\n\nNome: {self.name}\nDinheiro: ¥{self.money}\nPokébolas: {self.pokeballs}\nPokémons ({self.pokemons})\n")
    repetir = True
    while(repetir):
        playerPokemons()
        print("\n\nO que fazer?\n\n1- Deletar algum Pokémon\n2- Voltar ao menu")
        acao = input('\n\n')
        if acao == "1":
            if self.pokemons > 1:
                print("\n\nQual Pokémon você deseja excluir da sua party?")
                {playerPokemons()}
                print("0- Cancelar")
                excluirpoke = input("\n\n")
                if excluirpoke == "1":
                    print(f"\n\nVocê excluiu o Pokémon {pokemonsCapturados[0].species} da sua party.")
                    self.pokemons -= 1
                    pokemonsCapturados.pop(0)
                elif excluirpoke == "2":
                    print(f"\n\nVocê excluiu o Pokémon {pokemonsCapturados[0].species} da sua party.")
                    self.pokemons -= 1
                    pokemonsCapturados.pop(1)
                elif excluirpoke == "3":
                    print(f"\n\nVocê excluiu o Pokémon {pokemonsCapturados[0].species} da sua party.")
                    self.pokemons -= 1
                    pokemonsCapturados.pop(2)
                elif excluirpoke == "4":
                    print(f"\n\nVocê excluiu o Pokémon {pokemonsCapturados[0].species} da sua party.")
                    self.pokemons -= 1
                    pokemonsCapturados.pop(3)
                elif excluirpoke == "5":
                    print(f"\n\nVocê excluiu o Pokémon {pokemonsCapturados[0].species} da sua party.")
                    self.pokemons -= 1
                    pokemonsCapturados.pop(4)
                elif excluirpoke == "6":
                    print(f"\n\nVocê excluiu o Pokémon {pokemonsCapturados[0].species} da sua party.")
                    self.pokemons -= 1
                    pokemonsCapturados.pop(5)
                elif excluirpoke == "0":
                    break
                else:
                    print(f"Escolha um de seus {self.pokemons} Pokémons.")
            else:
                print("\n\nVocê possui apenas um Pokémon.")
        elif acao == "2":
            sleep(1)
            print("\n\nVocê voltou ao Menu.")
            sleep(1)
            break
        else:
            print("\n\nAção inválida. Tente novamente.")
            
def playerPokemons():
    n = 1
    for p in pokemonsCapturados:
        print(f"{n}- {p.species} ({p.hp}/{p.maxhp})")
        n+=1
        
def pokeCenter():
    sleep(1)
    print("\n\nVamos curar seus Pokémons. Aguarde...")
    sleep(1)
    print("\n...")
    sleep(1)
    for p in pokemonsCapturados:
        p.hp = p.maxhp
    print("\n\nSeus Pokémons agora estão com o HP cheio.")
    sleep(1)
    
def pokeShop(self):
    sleep(1)
    print("\n\nBem-vindo ao PokeShop. O que deseja fazer?\n\n1- Comprar\n2- Sair da Loja")
    repetir = True
    while(repetir):
        acao = input("\n\n")
        if acao == "1":
            repetir = True
            while(repetir):
                print(f"\n\nSeu dinheiro: ¥{self.money}\n\n1- Pokeball          ¥200\n0- Voltar")
                compra = input("\n\n")
                if compra == "1":
                    repetir = True
                    while(repetir):
                        quant = input("\n\nQuantidade: ")
                        if quant.isnumeric():
                            quant = int(quant)
                            if self.money < 200*quant:
                                sleep(1)
                                print("Você não tem dinheiro o suficiente.")
                                break
                            else:
                                sleep(1)
                                print(f"\n\nVocê comprou {quant} Pokébolas por ¥{quant*200}.")
                                self.money -= quant*200
                                self.pokeballs += quant
                                sleep(1)
                                print("\n\nDeseja comprar mais alguma coisa?")
                                break
                        else:
                            print("\n\nInsira a quantidade de itens que você deseja comprar.")
                elif compra == "0":
                    sleep(1)
                    print("\n\nO que deseja fazer?\n\n1- Comprar\n2- Sair da Loja")
                    break
                else:
                    print("\n\nItem inválido. Tente novamente.")
        elif acao == "2":
            sleep(1)
            print("\n\nVocê saiu da Loja.")
            sleep(1)
            break
        else:
            sleep(1)
            print("\n\nAção inválida. Tente novamente.")
        
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
