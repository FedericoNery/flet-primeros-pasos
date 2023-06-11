import flet as ft

from users_service import UsersService

users_service = UsersService()

def main(page: ft.Page):
    t = ft.Text(value="Hello!", color="green")
    page.add(t)

    users_list = users_service.get_users()

    lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)

    for user in users_list:
        name = user["name"]
        lv.controls.append(ft.Text(f"Nombre: {name}"))

    page.add(lv)

#ft.app(target=main)
ft.app(target=main, view=ft.WEB_BROWSER) #Si quieren iniciarlo en un navegador
#flet_example.app(port=8550, target=main) # alternativa para abrirlo en http://localhost:<port>