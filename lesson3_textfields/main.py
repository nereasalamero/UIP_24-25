import flet as ft


def main(page: ft.Page):
    page.title = "Lesson 3. Textfields, Buttons, and Dialogs"
    page.theme_mode = "light"
    page.horizontal_alignment = "center"

    # Text fields for name and university
    name = ft.TextField(label="Name", width=400, autofocus=True)
    university = ft.TextField(label="University", width=400)

    list_n = ft.Column()

    
    def print_list(e):
        list_n.controls.append(ft.Text(f"Hello {name.value} from {university.value}\n"))
        name.value = ""
        university.value = ""
        name.focus()
        page.update()

    def print_dialog(e):
        dialog = ft.AlertDialog(
            title=ft.Text(f"Hello {name.value} from {university.value}"), on_dismiss=lambda e: print("Dialog dismissed"),
            alignment="center"
        )
        page.overlay.append(dialog)
        dialog.open = True
        name.value = ""
        university.value = ""
        name.focus()
        page.update()


    # Buttons to print list and dialog
    list1 = ft.ElevatedButton("Print list", width=200, on_click=print_list)
    dialog1 = ft.ElevatedButton("Print dialog", width=200, on_click=print_dialog)

    page.add(name, university, ft.Row(controls=[list1, dialog1],alignment="center"), list_n)    

ft.app(main)
