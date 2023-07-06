import flet
from flet_core import Page, ThemeMode

from views.main_view import MainView


def main(page: Page):
    page.title = "Game Music Desktop"
    page.window_width = 900
    page.window_max_width = 900
    page.window_min_width = 900

    page.window_height = 600
    page.window_max_height = 600
    page.window_min_height = 600

    page.theme_mode = ThemeMode.DARK

    page.padding = 0

    page.fonts = {
        "JetBrainsMono": "fonts/JetBrainsMono.ttf",
    }

    page.add(MainView())


if __name__ == '__main__':
    flet.app(target=main)
