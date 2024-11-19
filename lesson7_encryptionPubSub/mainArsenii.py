import flet as ft

def main(page: ft.Page):
    page.title = "Encrypted PubSub Chat"
    page.vertical_alignment = ft.CrossAxisAlignment.CENTER

    def decrypt(message, key):
        if not key:
            return "Error: Passkey is empty."
        return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(message))

    # Function to handle incoming messages
    def on_message(encrypted_msg):
        if passkey_input.value:
            decrypted_msg = decrypt(encrypted_msg, passkey_input.value)
            messages.controls.append(ft.Text(decrypted_msg, color="blue"))
            page.update()
        else:
            messages.controls.append(ft.Text("Error: Passkey is missing for decryption.", color="red"))
            page.update()

    def subscribe_to_topic(e):
        page.pubsub.subscribe(on_message)
        page.update()

    def send_click(e):
        if not passkey_input.value:
            messages.controls.append(ft.Text("Error: Passkey is required to send a message.", color="red"))
            page.update()
            return

        passkey = passkey_input.value
        message_text = message.value
        user_name = user.value

        if not message_text or not user_name:
            messages.controls.append(ft.Text("Error: User name and message cannot be empty.", color="red"))
            page.update()
            return

        encrypted_msg = decrypt(f"{user_name}: {message_text}", passkey)
        page.pubsub.send_all(encrypted_msg)
        message.value = ""
        page.update()

    # Define UI components with labels
    user_label = ft.Text("Your Name:")
    user = ft.TextField(hint_text="Enter your name", width=300)

    publish_label = ft.Text("Publish Topic:")
    publish_to = ft.TextField(hint_text="Enter topic to publish to", width=300)

    subscribe_label = ft.Text("Subscribe to Topic:")
    subscribe_to = ft.Dropdown(
        width=300,
        options=[
            ft.dropdown.Option("music"),
            ft.dropdown.Option("sport"),
            ft.dropdown.Option("movie"),
        ],
        hint_text="Select a topic",
        on_change=subscribe_to_topic
    )

    passkey_label = ft.Text("Encryption Passkey:")
    passkey_input = ft.TextField(hint_text="Enter passkey", password=True, width=300)

    message_label = ft.Text("Message:")
    message = ft.TextField(hint_text="Type your message here...", width=300, multiline=True)

    send_button = ft.ElevatedButton("Send Message", on_click=send_click)

    # Define chat messages area with a heading
    messages_heading = ft.Text("Chat Messages", size=20, weight="bold", color="blue")
    messages = ft.ListView(expand=True)  # Utiliser ListView pour permettre le défilement

    # Add components to the page with organized layout
    page.add(
        ft.Column(
            [
                ft.Row([user_label, user, publish_label, publish_to]),
                ft.Row([subscribe_label, subscribe_to, passkey_label, passkey_input]),
                message_label,
                message,
                ft.Row([send_button], alignment=ft.MainAxisAlignment.CENTER),
                messages_heading,
                messages,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10,
            width=600  # Adjust width for layout consistency
        )
    )

ft.app(main, view=ft.AppView.WEB_BROWSER)