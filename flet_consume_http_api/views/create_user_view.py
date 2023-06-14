import flet as ft

import sys
# setting path
sys.path.append('..')

def create_user_view():
    return ft.View(
        controls=[
            ft.Text(value="Hello!", color="black"),
        ]
    )