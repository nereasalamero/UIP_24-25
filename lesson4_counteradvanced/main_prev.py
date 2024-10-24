import flet as ft

def main(page: ft.Page):
    page.title = "Flet counter example"

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

    def add_clicked(e):
        # Añadir una fila con la etiqueta con el nombre añadido en new_task y el contador, y un botón para eliminar la fila
        label = {new_task.value}
        delete_button = ft.IconButton(ft.icons.REMOVE, on_click=delete_clicked)
        tasks_view.controls.append(ft.Row(
            controls=[label, counter, delete_button],
            alignment=ft.MainAxisAlignment.CENTER
        ))
        new_task.value = ""
        view.update()

    def delete_clicked(e):
        tasks_view.controls.remove(e.source.parent)
        view.update()

    new_task = ft.TextField(hint_text="Enter a counter name", expand=True)
    tasks_view = ft.Column()
    view=ft.Column(
        width=600,
        controls=[
            ft.Row(
                controls=[
                    new_task,
                    ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_clicked)
                ],
            ),
            tasks_view,
        ],
    )
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.add(view)

    counter = ft.Row(
        [
            ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
            txt_number,
            ft.IconButton(ft.icons.ADD, on_click=plus_click),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )


class CounterApp(ft.Column):
    def __init__(self):
        super().__init__()
        
        self.controls = [
            ft.Row(
                controls = [
                    ft.IconButton(ft.icons.REMOVE, on_click=self.minus_click),
                    self.counter,
                    ft.IconButton(ft.icons.ADD, on_click=self.plus_click),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ]
    def add_clicked(self, e):
        # Añadir una fila con la etiqueta con el nombre añadido en new_task y el contador, y un botón para eliminar la fila
        label = new_task.value
        delete_button = ft.IconButton(ft.icons.REMOVE, on_click=delete_clicked)
        tasks_view.controls.append(ft.Row(
            controls=[label, counter, delete_button],
            alignment=ft.MainAxisAlignment.CENTER
        ))
        new_task.value = ""
        view.update()

    def delete_clicked(self, e):
        self.tasks_view.controls.remove(e.source.parent)
        self.update()


def main(page: ft.Page):
    page.title = "Counter App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    # Create application instance
    app_counter = CounterApp()
    page.add(app_counter)

ft.app(main)