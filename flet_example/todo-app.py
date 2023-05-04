import flet as ft

from widgets.card_pokemon import get_pokemon_card
from pokebase_service import obtener_pokemon

def main(page: ft.Page):
    # add/update controls on Page
    pokemon = obtener_pokemon(1)
    other = pokemon.sprites.other
    offial_artwork = getattr(other, "official-artwork")
    imagen_pokemon = offial_artwork.front_default
    t = ft.Text(value="Hello, world!", color="green")
    page.controls.append(t)
    page.update()

    card_pokemon = get_pokemon_card(imagen_pokemon)
    page.add(card_pokemon)


#ft.app(target=main)
ft.app(target=main, view=ft.WEB_BROWSER) #Si quieren iniciarlo en un navegador
#flet_example.app(port=8550, target=main) # alternativa para abrirlo en http://localhost:<port>


"""    page.add(
        ft.Row(controls=[
            ft.Text("A"),
            ft.Text("B"),
            ft.Text("C")
        ])
    )

    def button_clicked(e):
        page.add(ft.Text("Clicked!"))

    page.add(ft.ElevatedButton(text="Click me", on_click=button_clicked))"""

"""  img = ft.Image(
      src=imagen_pokemon,
      width=100,
      height=100,
      fit=ft.ImageFit.CONTAIN,
  )

  page.add(img)"""


"""
para hotreload
flet run main.py -d
"""