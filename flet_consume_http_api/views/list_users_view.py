import flet as ft

import sys
# setting path
sys.path.append('..')

from flet_consume_http_api.users_service import UsersService
from flet_consume_http_api.widgets.edit_user_button import edit_user_button
from flet_consume_http_api.widgets.view_user_button import view_user_button

def list_users_view(go_to_edit_user, go_to_detail_user):
    users_service_instance = UsersService()
    users_list = users_service_instance.get_users()

    lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
    for user in users_list:
        name = user["name"]
        id = user["id"]

        def view_user_function(e):
            go_to_detail_user(id)
        def edit_user_function(e):
            go_to_edit_user(id)

        row = ft.Row(controls=[
            ft.Text(f"ID: {id} Nombre: {name}"),
            view_user_button(view_user_function),
            edit_user_button(edit_user_function)
        ])

        lv.controls.append(row)

    return ft.Column(
        controls=[
            ft.Text(value="Listado de Usuarios", color="white", size=50),
            lv
        ]
    )
