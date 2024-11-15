import flet as ft

# Create a new task input
class Counter(ft.Column):
    def __init__(self):
        super().__init__()
        self.new_task = ft.TextField(hint_text="Add a new counter")
        self.tasks_view = ft.Column()
        self.width = 600
        self.controls = [
            ft.Row(
                controls = [
                    self.new_task,
                    ft.FloatingActionButton(icon=ft.icons.ADD, on_click=self.add_clicked),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            self.tasks_view,
        ]

    # Change the increment/decrement 1 to the value of the counter
    def minus_click(self, e, txt_number):
        txt_number.value = str(int(txt_number.value) - 1)
        self.update()

    def plus_click(self, e, txt_number):
        txt_number.value = str(int(txt_number.value) + 1)
        self.update()

    def delete_clicked(self, counter_container):
        self.tasks_view.controls.remove(counter_container)
        self.update()

    def add_clicked(self, e):
        label = ft.Text(self.new_task.value)
        txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)
        counter = ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=lambda e: self.minus_click(e, txt_number)),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=lambda e: self.plus_click(e, txt_number)),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
        counter_container = ft.Row(
            controls=[label, counter],
            alignment=ft.MainAxisAlignment.CENTER,
        )
        delete_button = ft.IconButton(ft.icons.DELETE, on_click=lambda e: self.delete_clicked(counter_container))

        self.tasks_view.controls.append(ft.Row(
            controls=[counter_container, delete_button],
            alignment=ft.MainAxisAlignment.END,
        ))
        self.new_task.value = ""
        self.update()


def main(page: ft.Page):
    page.title = "Counter App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Create application instance
    app_counter = Counter()
    page.add(app_counter)

ft.app(target=main)