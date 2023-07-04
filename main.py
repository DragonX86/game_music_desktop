import flet
from flet import WEB_BROWSER
from flet_core import Page, ThemeMode

from pages.main_page import MainPage


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

    page.add(MainPage())


if __name__ == '__main__':
    flet.app(target=main)
