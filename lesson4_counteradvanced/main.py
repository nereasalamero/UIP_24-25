import flet as ft
from flet import UserControl

# Create a new task input
class CounterApp(UserControl):
    counter = 0
    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)
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

    # Change the increment/decrement to 2^n (where n is every increase or decrease in integer values)
    def minus_click(self, e):
        self.txt_number.value = str(pow(2, self.counter-1))
        self.counter -= 1
        self.update()

    def plus_click(self, e):
        self.txt_number.value = str(pow(2,self.counter+1))
        self.counter += 1
        self.update()
    
    def add_clicked(self, e):
        self.label = {self.new_task.value}
        self.delete_button = ft.IconButton(ft.icons.REMOVE, on_click=self.delete_clicked)
        self.counter = ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=self.minus_click),
                self.txt_number,
                ft.IconButton(ft.icons.ADD, on_click=self.plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
        self.tasks_view.controls.append(ft.Row(
            controls=[self.label, self.counter, self.delete_button],
            alignment=ft.MainAxisAlignment.CENTER
        ))
        self.new_task.value = ""
        self.update()

    def delete_clicked(self, e):
        self.tasks_view.controls.remove(e.source.parent)
        self.update()


def main(page: ft.Page):
    page.title = "Counter App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    app = CounterApp()
    app.initialize()

    # Create application instance
    # app_counter = CounterApp()
    # page.add(app_counter)
    page.add(app)
    page.update()

ft.app(target=main)