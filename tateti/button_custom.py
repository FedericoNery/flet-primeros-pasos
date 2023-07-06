import flet as ft
from flet_core import RoundedRectangleBorder, BorderSide


def button_custom(identificador, tateti, actualizar_ui):
    ref_elevated_button = ft.Ref[ft.ElevatedButton]()
    ref_text = ft.Ref[ft.Text]()

    def on_click(event):
        ref_elevated_button.current.disabled = True
        ref_elevated_button.current.content = ft.Text(tateti.aplicar_jugada(identificador), ref=ref_text, color=ft.colors.BLACK, size=40)
        if
        actualizar_ui()

    return ft.ElevatedButton(ref=ref_elevated_button,
                             width=200,
                             height=200,
                                  style=ft.ButtonStyle(
                                      shape=RoundedRectangleBorder(),
                                      padding=60,
                                      bgcolor={
                                          ft.MaterialState.HOVERED: ft.colors.YELLOW_300,
                                          #ft.MaterialState.FOCUSED: ft.colors.BLUE_GREY,
                                          ft.MaterialState.DISABLED: ft.colors.YELLOW_50,
                                          ft.MaterialState.DEFAULT: ft.colors.YELLOW,
                                      },
                                      side={
                                          ft.MaterialState.HOVERED: BorderSide(3, ft.colors.RED),
                                      },
                                  ),

                         content=ft.Text(" ", ref=ref_text, color=ft.colors.BLACK, size=40),
                             on_click=on_click)


# overlay_color=ft.colors.YELLOW_300,

"""color={
    ft.MaterialState.HOVERED: ft.colors.BLACK,
    ft.MaterialState.FOCUSED: ft.colors.BLACK,
    ft.MaterialState.DEFAULT: ft.colors.BLACK,
},"""