import flet as ft

def create_user_button(go_to_create_user):
    return ft.FloatingActionButton(
        content=ft.Row(
            [ft.Icon(ft.icons.ADD), ft.Text("Add")], alignment="center", spacing=5
        ),
        bgcolor=ft.colors.BLACK,
        shape=ft.RoundedRectangleBorder(radius=5),
        width=100,
        mini=True,
        on_click=go_to_create_user
    )
