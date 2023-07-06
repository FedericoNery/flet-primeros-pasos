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

    c1 = button_custom(0, tateti, actualizar_ui)

    c2 = button_custom(1, tateti, actualizar_ui)

    c3 = button_custom(2, tateti, actualizar_ui)

    c4 = button_custom(3, tateti, actualizar_ui)

    c5 = button_custom(4, tateti, actualizar_ui)

    c6 = button_custom(5, tateti, actualizar_ui)

    c7 = button_custom(6, tateti, actualizar_ui)

    c8 = button_custom(7, tateti, actualizar_ui)

    c9 = button_custom(8, tateti, actualizar_ui)

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


ft.app(target=main)