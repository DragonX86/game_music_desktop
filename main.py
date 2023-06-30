import flet
from flet_core import Page, ThemeMode

from views.simple_view import SimpleView


def main(page: Page):
    page.title = "Flet counter example"
    page.window_width = 800
    page.window_height = 500

    page.theme_mode = ThemeMode.LIGHT

    page.padding = 0

    page.add(
        SimpleView()
    )


flet.app(target=main)
