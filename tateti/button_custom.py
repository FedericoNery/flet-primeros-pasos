import flet as ft

def button_custom(identificador, tateti, actualizar_ui):
    ref = ft.Ref[ft.OutlinedButton]()

    def on_click(event):
        ref.current.text = tateti.aplicar_jugada(identificador)
        ref.current.disabled = True
        actualizar_ui()

    return ft.OutlinedButton(" ",ref=ref,
                                  style=ft.ButtonStyle(
                                      color={
                                          ft.MaterialState.HOVERED: ft.colors.BLUE_GREY,
                                          ft.MaterialState.FOCUSED: ft.colors.BLUE,
                                          ft.MaterialState.DEFAULT: ft.colors.BLACK,
                                      },
                                  ),
                             on_click=on_click)