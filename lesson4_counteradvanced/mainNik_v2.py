import flet as ft

class Counter:
    def __init__(self, name):
        self.count = 0  
        self.name = name  

    def add_one(self):
        self.count += 1  

    def subtract_one(self):
        self.count -= 1  

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT    
    page.horizontal_alignment = "center"

    counters = []  

    def add_counter(e):
        counter_name = name_input.value
        if counter_name:  
            new_counter = Counter(counter_name)  
            counters.append(new_counter)  

            counter_row = ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,  
                controls=[
                    ft.Text(new_counter.name),  
                    ft.Text(f" Count: {new_counter.count}"), 
                    ft.IconButton(ft.icons.DELETE, on_click=lambda e: remove_counter(counter_container))  
                ]
            )

            def plus_button_pressed(e):
                new_counter.add_one()  
                counter_row.controls[1] = ft.Text(f" Count: {new_counter.count}")  
                page.update()  

            def minus_button_pressed(e):
                new_counter.subtract_one()  
                counter_row.controls[1] = ft.Text(f" Count: {new_counter.count}")  
                page.update()  

            button_row = ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[ 
                    ft.ElevatedButton("+", on_click=plus_button_pressed),  
                    ft.ElevatedButton("-", on_click=minus_button_pressed) 
                ]
            )

            # Create a container for the counter and its buttons
            counter_container = ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,  
                controls=[
                    counter_row,
                    button_row  
                ]
            )

            page.add(counter_container)
            page.update()  
            name_input.value = ""  

    def remove_counter(counter_container):
        page.controls.remove(counter_container)
        page.update()  

    name_input = ft.TextField(label="Counter Name", width=200)

    page.add(
        ft.Column([
            name_input,  
            ft.ElevatedButton("Add Counter", on_click=add_counter)  
        ])
    )

ft.app(main)
