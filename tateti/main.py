import flet as ft

from button_custom import button_custom
from tateti import Tateti


def main(page: ft.Page):
    page.title = "Containers with background color"
    page.padding = 50
    tateti = Tateti()

    def actualizar_ui():
        page.update()

    c1 = ft.Container(
        content=button_custom(0, tateti, actualizar_ui),
        bgcolor=ft.colors.YELLOW,
        padding=20,
    )

    c2 = ft.Container(
        content=button_custom(1, tateti, actualizar_ui),
        bgcolor=ft.colors.YELLOW,
        padding=20,
    )

    c3 = ft.Container(
        content=button_custom(2, tateti, actualizar_ui),
        bgcolor=ft.colors.YELLOW,
        padding=20,
    )
    c4 = ft.Container(
        content=button_custom(3, tateti, actualizar_ui),
        bgcolor=ft.colors.YELLOW,
        padding=20,
    )

    c5 = ft.Container(
        content=button_custom(4, tateti, actualizar_ui),
        bgcolor=ft.colors.YELLOW,
        padding=20,
    )

    c6 = ft.Container(
        content=button_custom(5, tateti, actualizar_ui),
        bgcolor=ft.colors.YELLOW,
        padding=20,
    )

    c7 = ft.Container(
        content=button_custom(6, tateti, actualizar_ui),
        bgcolor=ft.colors.YELLOW,
        padding=20,
    )

    c8 = ft.Container(
        content=button_custom(7, tateti, actualizar_ui),
        bgcolor=ft.colors.YELLOW,
        padding=20,
    )

    c9 = ft.Container(
        content=button_custom(8, tateti, actualizar_ui),
        bgcolor=ft.colors.YELLOW,
        padding=20,
    )

    row1 = ft.Row(
        controls=[
            c1,
            c2,
            c3
        ]
    )

    row2 = ft.Row(
        controls=[
            c4,
            c5,
            c6
        ]
    )

    row3 = ft.Row(
        controls=[
            c7,
            c8,
            c9
        ]
    )

    page.add(row1)
    page.add(row2)
    page.add(row3)


ft.app(target=main)