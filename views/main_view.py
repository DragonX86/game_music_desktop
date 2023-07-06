from flet_core import Column, Row, Container, alignment, colors, Text, TextField, margin, TextButton, ButtonStyle, \
    RoundedRectangleBorder, FontWeight, Ref, TextStyle, icons, IconButton, MainAxisAlignment, Image, ImageFit, \
    border_radius, border, Slider


def MainView():
    data = {'play_status': False, 'repeat_status': False, 'shuffle_status': False}

    name_textfield = Ref[TextField]()

    def change_play_status(event):
        data['play_status'] = not data['play_status']

        event.control.selected = not event.control.selected
        event.control.update()

    def change_repeat_status(event):
        data['repeat_status'] = not data['repeat_status']

        event.control.selected = not event.control.selected
        event.control.update()

    def change_shuffle_status(event):
        data['shuffle_status'] = not data['shuffle_status']

        event.control.selected = not event.control.selected
        event.control.update()

    def on_click_handler(_):
        data['query'] = name_textfield.current.value
        name_textfield.current.value = ""

        name_textfield.current.page.update()
        print(data)

    return Column(
        spacing=0,
        controls=[
            Row(
                controls=[
                    Container(
                        alignment=alignment.center,
                        margin=margin.only(left=10, top=10, bottom=10, right=5),
                        content=TextField(
                            filled=True,
                            ref=name_textfield,
                            label="Введите название:",
                            label_style=TextStyle(
                                size=14,
                                weight=FontWeight.W_400,
                                italic=True
                            ),
                            text_style=TextStyle(
                                size=14,
                                weight=FontWeight.W_300,
                                font_family="JetBrainsMono"
                            ),
                            border_color=colors.LIGHT_GREEN_800
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
                            on_click=on_click_handler,
                            text="Начать поиск"
                        ),
                        expand=20
                    ),
                ],
                spacing=0,
                expand=13
            ),
            Row(
                controls=[],
                spacing=0,
                expand=70
            ),
            Row(
                spacing=0,
                controls=[
                    Row(
                        spacing=0,
                        controls=[
                            IconButton(
                                icon=icons.SKIP_PREVIOUS,
                                icon_color=colors.GREY,
                                icon_size=30,
                            ),
                            IconButton(
                                selected=False,
                                icon=icons.PLAY_ARROW,
                                icon_color=colors.GREY,
                                selected_icon=icons.PAUSE,
                                selected_icon_color=colors.GREY,
                                on_click=change_play_status,
                                icon_size=30,
                            ),
                            IconButton(
                                icon=icons.SKIP_NEXT,
                                icon_color=colors.GREY,
                                icon_size=30,
                            )
                        ],
                        alignment=MainAxisAlignment.CENTER,
                        expand=20
                    ),
                    Row(

                        spacing=0,
                        controls=[
                            Container(
                                border=border.all(2, colors.LIGHT_GREEN_800),
                                border_radius=border_radius.all(5),
                                content=Image(
                                    fit=ImageFit.CONTAIN,
                                    src="https://legatomusic.ru/nas/h250/img/cdimg2/00/94/68/70.jpg",
                                    border_radius=border_radius.all(5),
                                    height=60,
                                    width=60
                                ),
                            ),
                            Column(
                                spacing=0,
                                controls=[
                                    Container(
                                        content=Slider(
                                            thumb_color=colors.LIGHT_GREEN_800,
                                            active_color=colors.LIGHT_GREEN_800,
                                            min=0, max=1000, label="{value}%"
                                        ),
                                        expand=15
                                    ),
                                    Container(
                                        padding=0,
                                        alignment=alignment.top_center,
                                        content=Column(
                                            spacing=0,
                                            controls=[
                                                Text("Music Track Title", size=12),
                                                Text("Music Album Title", size=12)
                                            ]
                                        ),
                                        expand=20
                                    )
                                ],
                                expand=True
                            ),
                        ],
                        expand=60
                    ),
                    Row(
                        spacing=0,
                        alignment=MainAxisAlignment.START,
                        controls=[
                            IconButton(
                                icon=icons.SHUFFLE,
                                icon_color=colors.GREY,
                                selected_icon=icons.SHUFFLE,
                                selected_icon_color=colors.LIGHT_GREEN_800,
                                on_click=change_shuffle_status,
                                icon_size=30
                            ),
                            IconButton(
                                icon=icons.REPEAT,
                                icon_color=colors.GREY,
                                selected_icon=icons.REPEAT_ONE,
                                selected_icon_color=colors.LIGHT_GREEN_800,
                                on_click=change_repeat_status,
                                icon_size=30
                            ),
                            IconButton(
                                icon=icons.DOWNLOAD,
                                icon_color=colors.GREY,
                                icon_size=30
                            )
                        ],
                        expand=20
                    ),
                ],
                expand=17
            )
        ],
        expand=True
    )
