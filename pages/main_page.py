from flet_core import Column, Row, Container, alignment, colors, Text, TextField, margin, TextButton, ButtonStyle, \
    RoundedRectangleBorder, TextStyle, FontWeight


def MainPage():
    def on_submit_handler(event):
        print(event.control.label_style)

    return Column(
        controls=[
            Row(
                controls=[
                    Container(
                        alignment=alignment.center,
                        margin=margin.only(left=10, top=10, bottom=10, right=5),
                        content=TextField(
                            filled=True,
                            label="Введите название:",
                            label_style=TextStyle(
                                size=14,
                                weight=FontWeight.W_400,
                                italic=True
                            ),
                            text_style=TextStyle(
                                size=14,
                                weight=FontWeight.W_500
                            ),
                            on_submit=on_submit_handler,
                            border_color=colors.LIGHT_GREEN_800,
                        ),
                        expand=80
                    ),
                    Container(
                        width=float("inf"),
                        height=float("inf"),
                        margin=margin.only(left=5, top=10, bottom=10, right=10),
                        content=TextButton(
                            style=ButtonStyle(
                                bgcolor=colors.LIGHT_GREEN_800,
                                shape=RoundedRectangleBorder(radius=5)
                            ),
                            text="Начать поиск"
                        ),
                        expand=20
                    ),
                ],
                spacing=0,
                expand=12
            ),
            Row(
                controls=[
                    Container(
                        padding=12,
                        bgcolor=colors.BLUE_600,
                        alignment=alignment.center,
                        content=Text("Container 1"),
                        expand=1
                    ),
                ],
                spacing=0,
                expand=70
            ),
            Row(
                controls=[
                    Container(
                        padding=12,
                        bgcolor=colors.GREY_400,
                        alignment=alignment.center,
                        content=Text("Container 1"),
                        expand=2
                    ),
                ],
                spacing=0,
                expand=18
            )
        ],
        spacing=0,
        expand=True
    )
