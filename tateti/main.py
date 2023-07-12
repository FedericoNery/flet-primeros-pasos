import flet as ft
from flet_core import MainAxisAlignment

from button_custom import button_custom
from tateti import Tateti


def main(page: ft.Page):
    page.title = "Containers with background color"
    page.padding = 50
    page.vertical_alignment = MainAxisAlignment.CENTER
    tateti = Tateti()

    def actualizar_ui():
        page.update()

    def reset(event):
        tateti.resetear_juego()
        c1.disabled = False
        c2.disabled = False
        c3.disabled = False
        c4.disabled = False
        c5.disabled = False
        c6.disabled = False
        c7.disabled = False
        c8.disabled = False
        c9.disabled = False
        reset_textos()

    def reset_textos():
        c1.content = ft.Text("")
        c2.content = ft.Text("")
        c3.content = ft.Text("")
        c4.content = ft.Text("")
        c5.content = ft.Text("")
        c6.content = ft.Text("")
        c7.content = ft.Text("")
        c8.content = ft.Text("")
        c9.content = ft.Text("")
        mensaje.visible = False
        actualizar_ui()
    def termino_el_juego_ui(ganador):
        #reset_textos()
        c1.disabled = True
        c2.disabled = True
        c3.disabled = True
        c4.disabled = True
        c5.disabled = True
        c6.disabled = True
        c7.disabled = True
        c8.disabled = True
        c9.disabled = True
        mensaje.value = f"El ganador fue: {ganador}"
        mensaje.visible = True
        actualizar_ui()

    c1 = button_custom(0, tateti, actualizar_ui, termino_el_juego_ui)

    c2 = button_custom(1, tateti, actualizar_ui, termino_el_juego_ui)

    c3 = button_custom(2, tateti, actualizar_ui, termino_el_juego_ui)

    c4 = button_custom(3, tateti, actualizar_ui, termino_el_juego_ui)

    c5 = button_custom(4, tateti, actualizar_ui, termino_el_juego_ui)

    c6 = button_custom(5, tateti, actualizar_ui, termino_el_juego_ui)

    c7 = button_custom(6, tateti, actualizar_ui, termino_el_juego_ui)

    c8 = button_custom(7, tateti, actualizar_ui, termino_el_juego_ui)

    c9 = button_custom(8, tateti, actualizar_ui, termino_el_juego_ui)

    button_reset = ft.ElevatedButton("Reset", on_click=reset)

    mensaje = ft.Text("")
    mensaje.visible = False

    row1 = ft.Row(
        controls=[
            c1,
            c2,
            c3
        ],
        alignment= MainAxisAlignment.CENTER
    )

    row2 = ft.Row(
        controls=[
            c4,
            c5,
            c6
        ],
        alignment=MainAxisAlignment.CENTER
    )

    row3 = ft.Row(
        controls=[
            c7,
            c8,
            c9
        ],
        alignment=MainAxisAlignment.CENTER
    )

    page.add(row1)
    page.add(row2)
    page.add(row3)
    page.add(button_reset)
    page.add(mensaje)

ft.app(target=main)