from flet import Card, Container, Column, Row, Image, ListTile, \
    ImageFit, Text, MainAxisAlignment, FilledButton


def get_pokemon_card(imagen_pokemon):
    return Card(
        content=Container(
            content=Column(
                [
                    Row(
                        [
                            Image(
                                src=imagen_pokemon,
                                width=100,
                                height=100,
                                fit=ImageFit.CONTAIN,
                            ),
                            ListTile(
                                title=Text("The Enchanted Nightingale"),
                            )
                        ],
                        alignment=MainAxisAlignment.START,
                    ),
                    Row(
                        [
                            FilledButton("Disabled button", disabled=True),
                            FilledButton("Disabled button", disabled=True)
                        ],
                        alignment=MainAxisAlignment.END,
                    ),
                ]
            ),
            width=400,
            padding=10,
        )
    )

