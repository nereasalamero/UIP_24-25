import flet as ft

def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    counter = 0

    # Change the increment/decrement to 2^n (where n is every increase or decrease in integer values)
    def minus_click(e):
        nonlocal counter
        txt_number.value = str(pow(2,counter-1))
        counter -= 1
        page.update()

    def plus_click(e):
        nonlocal counter
        txt_number.value = str(pow(2,counter+1))
        counter += 1
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )


ft.app(main)
