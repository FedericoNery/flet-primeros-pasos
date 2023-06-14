import flet as ft

import sys
# setting path
sys.path.append('..')

from flet_consume_http_api.users_service import UsersService


def list_users_view():
    users_service_instance = UsersService()
    users_list = users_service_instance.get_users()

    lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
    for user in users_list:
        name = user["name"]
        lv.controls.append(ft.Text(f"Nombre: {name}"))

    """return ft.View(
        controls=[
            ft.Text(value="Hello!", color="green"),
            lv
        ]
    )"""
    return ft.Column(
        controls=[
            ft.Text(value="Hello!", color="green"),
            lv
        ]
    )
