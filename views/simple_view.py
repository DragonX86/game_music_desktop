from flet_core import Column, Container, alignment, colors, Text, ElevatedButton, Ref


def SimpleView():
    last_name = Ref[Container]()

    def btn_click(_):
        if last_name.current.visible:
            last_name.current.visible = False
        else:
            last_name.current.visible = True

        last_name.current.update()

    return Column(
        controls=[
            Container(
                expand=8,
                ref=last_name,
                alignment=alignment.center,
                content=Text("Container 1"),
            ),
            Container(
                expand=2,
                alignment=alignment.center,
                content=Text("Container 2")
            ),
            Container(
                alignment=alignment.top_center,
                padding=8,
                content=ElevatedButton("Show Container 1", on_click=btn_click),
                bgcolor=colors.RED,
                expand=2,
            ),
        ],
        spacing=0,
        expand=True
    )
