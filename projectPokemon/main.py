import pokemonPokemons
import pokemonTrainers
import pokemonMethods

jogador = pokemonTrainers.Player(input("\n\nQual o seu nome? "), 0, 500, 5)
pokemonMethods.sleep(1)
print(f"\n\nOlá {jogador.name}. Sua jornada começará agora.")
pokemonMethods.sleep(1)
print("\n\nPrimeiro, vamos escolher um Pokémon inicial.\n\nEscolha entre os 3 Pokémons:")
repetir = True
while(repetir):
    repetir = False
    pokemonMethods.sleep(1)
    inicial = input("\n1- Bulbasaur\n2- Squirtle\n3- Charmander\n\n")
    pokemonMethods.sleep(1)
    if inicial == "1":
        pokemonPokemons.pokemonsCapturados.append(pokemonPokemons.Bulbasaur)
        jogador.pokemons += 1
    elif inicial == "2":
        pokemonPokemons.pokemonsCapturados.append(pokemonPokemons.Squirtle)
        jogador.pokemons += 1
    elif inicial == "3":
        pokemonPokemons.pokemonsCapturados.append(pokemonPokemons.Charmander)
        jogador.pokemons += 1
    else:
        print("\n\nAlgo deu errado, tente novamente.")
        repetir = True
        
print(f"\n\nVocê escolheu o Pokémon {pokemonPokemons.pokemonsCapturados[0].species} como seu inicial.")
pokemonMethods.sleep(1)
pokemonMethods.menu(jogador)
