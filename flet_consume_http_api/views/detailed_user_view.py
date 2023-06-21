import flet as ft
from flet_consume_http_api.users_service import UsersService

def detailed_user_view(id_user):
    users_service = UsersService()

    user = users_service.get_user_by(id_user)

    return ft.View(controls=[
        ft.Text(f"Nombre: {user['name']}", size=50),
        ft.Text(f"Edad: {user['age']}", size=30)
    ])