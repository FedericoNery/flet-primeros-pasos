import flet as ft
from flet_core import TemplateRoute

from views.list_users_view import list_users_view
from views.create_user_view import create_user_view
from views.detailed_user_view import detailed_user_view
from views.edit_user_view import edit_user_view

from widgets.create_user_button import create_user_button


def main(page: ft.Page):
    page.title = "Usuarios CRUD"

    def route_change(event):
        page.views.clear()
        troute = TemplateRoute(event.route)

        if event.route == "/create/user":
            print("INGRESO AL CREATE")
            create_user = create_user_view(go_to_list_users)
            page.views.append(create_user)

        elif troute.match("/users/:id/detail"):
            print("INGRESO AL DEATILED")

            detailed_user = detailed_user_view(troute.id)
            page.views.append(detailed_user)

        elif troute.match("/users/:id"):
            print("INGRESO AL EDIT")

            edit_user = edit_user_view(troute.id, go_to_list_users)
            page.views.append(edit_user)

        elif event.route == "/":
            print("INGRESO AL /")

            lu_view = list_users_view(go_to_edit_user, go_to_detail_user)
            create_user_btn = create_user_button(go_to_create_user)
            view = ft.View(controls=[
                lu_view,
                create_user_btn
            ])
            page.views.append(view)

        page.update()

    def go_to_create_user(e):
        page.route = "/create/user"
        page.update()

    def go_to_edit_user(id):
        page.route = f"/users/{id}"
        page.update()

    def go_to_detail_user(id):
        page.route = f"/users/{id}/detail"
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
    def go_to_list_users():
        page.route = "/"
        page.update()

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


# ft.app(target=main)
ft.app(target=main, view=ft.WEB_BROWSER)  # Si quieren iniciarlo en un navegador
# flet_example.app(port=8550, target=main) # alternativa para abrirlo en http://localhost:<port>
