import flet as ft

def view_user_button(onclick):
    return ft.IconButton(
        icon=ft.icons.ZOOM_IN,
        icon_color="blue400",
        icon_size=20,
        tooltip="View user",
        on_click=onclick
    )