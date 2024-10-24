import flet as ft
import datetime

def main(page: ft.Page):
    page.title = "Navigation and Routing"

    def handle_change(e):
        page.add(ft.Text(f"Date changed: {e.control.value.strftime('%Y-%m-%d')}"))

    def handle_dismissal(e):
        page.add(ft.Text(f"DatePicker dismissed"))

    name=ft.TextField(label="Name: ")
    date=ft.DatePicker(
        value=datetime.date.today(),
        on_change=handle_change,
        on_dismiss=handle_dismissal,
    )
    sex = ft.RadioGroup(content=ft.Row([
        ft.Radio(value="Female", label="Female"),
        ft.Radio(value="Male", label="Male"),
        ft.Radio(value="Other", label="Other"),]))
    address=ft.TextField(label="Address: ")
    
    country=ft.Dropdown(label="Country: ",
                width=100,
                options=[
                    ft.dropdown.Option("Finland"),
                    ft.dropdown.Option("Sweden"),
                    ft.dropdown.Option("Norway"),
                    ft.dropdown.Option("USA"),
                    ft.dropdown.Option("Spain"),
                    ft.dropdown.Option("France"),
                    ft.dropdown.Option("Other"),
                ])
    username = ft.TextField(label="Username")
    password = ft.TextField(label="Password", password=True, can_reveal_password=True)

    def validate_form(e):
        has_error = False
        # Check username
        if not username.value:
            username.error_text="The username is required"
            has_error=True
        else:
            username.error_text=None
        # Check password
        if not password.value:
            password.error_text="The password is required"
            has_error=True
        else:
            password.error_text=None
        username.update()
        password.update()
        # If there isn't any problem, it goes to forms
        if not has_error:
            page.go("/form")
    
    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text("Navigation and Routing"), bgcolor=ft.colors.SURFACE_VARIANT),
                    username,
                    password,
                    ft.ElevatedButton("Login", on_click=validate_form),                     
                ],
            )
        )
        if page.route == "/form":
            page.views.append(
                ft.View(
                    "/form",
                    [
                        ft.AppBar(title=ft.Text("Form"), bgcolor=ft.colors.SURFACE_VARIANT),
                        name,
                        ft.Text("Birth date"),
                        ft.ElevatedButton(
                            "Date",
                            icon=ft.icons.CALENDAR_MONTH,
                            on_click=lambda e: page.open(
                                date,
                            ),
                        ),
                        ft.Text("Sex: "),
                        sex,
                        address,
                        country,
                        ft.ElevatedButton("Show Details", on_click=lambda _: page.go("/showdetails")),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                    ],
                )
            )
        if page.route == "/showdetails":
            page.views.append(
                ft.View(
                    "/showdetails",
                    [
                        ft.AppBar(title=ft.Text("Show Details"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Card(
                            content=ft.Container(
                                content=ft.Column(
                                    [
                                        ft.Text(f"Name: {name.value}"),
                                        ft.Text(f"Birth date: {date.value.day}-{date.value.month}-{date.value.year}"),
                                        ft.Text(f"Sex: {sex.value}"),
                                        ft.Text(f"Address: {address.value}"),
                                        ft.Text(f"Country: {country.value}"),
                                        
                                        ft.Row(
                                            [
                                                ft.ElevatedButton("Return to form", on_click=lambda _: page.go("/form"))
                                            ],
                                            alignment=ft.MainAxisAlignment.END,
                                        ),
                                    ],
                                ),
                                width=400,
                                padding=10,
                            )),
                    ],
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(main, view=ft.AppView.WEB_BROWSER)