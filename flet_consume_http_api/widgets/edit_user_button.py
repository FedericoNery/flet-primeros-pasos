import flet as ft

def edit_user_button(onclick):
    return ft.IconButton(
        icon=ft.icons.EDIT_ROUNDED,
        icon_color="blue400",
        icon_size=20,
        tooltip="Edit user",
        on_click=onclick
    )