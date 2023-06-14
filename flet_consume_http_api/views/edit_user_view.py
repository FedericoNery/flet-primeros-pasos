import flet as ft

import sys

# setting path
sys.path.append('..')

from flet_consume_http_api.users_service import UsersService


def edit_user_view(id_user):
    users_service = UsersService()

    user = users_service.get_user_by(id_user)

    nombre_text_field = ft.TextField(label="Nombre", hint_text="Ingrese su nombre:")
    nombre_text_field.value = user["name"]
    edad_text_field = ft.TextField(label="Edad", hint_text="Ingrese su edad:")
    edad_text_field.value = user["age"]

    def on_click(e):
        nombre_user = nombre_text_field.value
        edad_user = int(edad_text_field.value)
        users_service.update_user(id_user, {
            "name": nombre_user,
            "age": edad_user
        })

    actualizar_button = ft.FilledButton(text="Actualizar", on_click=on_click)

    return ft.View(
        controls=[
            ft.Text(value="Actualizar Usuario", color="white", size=50),
            nombre_text_field,
            edad_text_field,
            actualizar_button
        ]
    )
