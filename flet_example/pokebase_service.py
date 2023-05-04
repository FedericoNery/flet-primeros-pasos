import pokebase
from pokebase import cache

cache.API_CACHE

"""
MOCKUPS PARA GUIARSE CON EL DISEÑO
https://dribbble.com/shots/6545819-Pokedex-App
"""


def obtener_nombres_y_urls_pokemon():
    respuesta_pokemon_resource_list = pokebase.APIResourceList("pokemon")
    lista_pokemon = []
    contador = 1
    for pokemon in respuesta_pokemon_resource_list:
        lista_pokemon.append({"nombre": pokemon["name"], "url": pokemon["url"], "numero": contador})
        contador += 1
    """for indice in range(respuesta_pokemon_resource_list.count):
        nombre = respuesta_pokemon_resource_list.names[indice]
        url = respuesta_pokemon_resource_list.urls[indice]
        lista_pokemon.append({ "nombre": nombre, "url": url, "numero": indice })"""
    return lista_pokemon


def obtener_pokemon(numero):
    pokemon = pokebase.pokemon(numero)
    """
    Que atributos tiene pokemon
    corroborarlo en esta página, pueden poner la url o ingresar a pokeapi.co y usar la UI para buscar
    https://pokeapi.co/api/v2/pokemon/1
    """

    """
    props esenciales

    name
    types -> array de diccionario con claves slot y type -> type tiene un atributo name type.name
    sprites -> other -> official-artwork -> front_default -> esto nos da la url de la imagen
    sprites.other.official-artwork.front_default
    """
    return pokemon


def obtener_los_n_pokemon(numero):
    pokemons = []
    for indice in range(numero):
        pokemon = obtener_pokemon(indice + 1)
        pokemons.append(pokemon)
    return pokemons

# obtener_nombres_y_urls_pokemon()
