import flet as ft


def main(page: ft.Page):
    page.add(ft.SafeArea(ft.Text("Hello IoT!", style=ft.TextStyle(color="blue"), style=ft.TextStyle(font_size=35))))


ft.app(main)
