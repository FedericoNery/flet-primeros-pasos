import flet as ft

from views.list_users_view import list_users_view
from views.create_user_view import create_user_view


def main(page: ft.Page):
    page.title = "Usuarios CRUD"
    def route_change(route):
        page.views.clear()
        if page.route == "/":
            lu_view = list_users_view()
            view = ft.View(controls=[
                lu_view,
                ft.FloatingActionButton(
                    content=ft.Row(
                        [ft.Icon(ft.icons.ADD), ft.Text("Add")], alignment="center", spacing=5
                    ),
                    bgcolor=ft.colors.BLACK,
                    shape=ft.RoundedRectangleBorder(radius=5),
                    width=100,
                    mini=True,
                    on_click=go_to_create_user
                )
            ])
            page.views.append(view)

        if page.route == "/create/user":
            create_user = create_user_view()
            page.views.append(create_user)
        page.update()

    def go_to_create_user(e):
        page.route = "/create/user"
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

#ft.app(target=main)
ft.app(target=main, view=ft.WEB_BROWSER) #Si quieren iniciarlo en un navegador
#flet_example.app(port=8550, target=main) # alternativa para abrirlo en http://localhost:<port>