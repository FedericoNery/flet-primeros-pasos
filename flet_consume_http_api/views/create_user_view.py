import flet as ft

import sys

# setting path
sys.path.append('..')

from flet_consume_http_api.users_service import UsersService

def create_user_view(go_to_list_users):
    nombre_text_field = ft.TextField(label="Nombre", hint_text="Ingrese su nombre:")

    edad_text_field = ft.TextField(label="Edad", hint_text="Ingrese su edad:")

    def on_click(e):
        users_service = UsersService()
        nombre_user = nombre_text_field.value
        edad_user = int(edad_text_field.value)
        users_service.save_user({
            "name": nombre_user,
            "age": edad_user
        })
        go_to_list_users()

    crear_button = ft.FilledButton(text="Crear", on_click=on_click)

    return ft.View(
        controls=[
            ft.Text(value="Crear Usuario", color="white", size=50),
            nombre_text_field,
            edad_text_field,
            crear_button
        ]
    )