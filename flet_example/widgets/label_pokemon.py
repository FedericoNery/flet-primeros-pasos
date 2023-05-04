from flet import ListTile, Text


def get_label_pokemon(nombre="Pokemon"):
    return ListTile(
        title=Text(nombre),
    )
