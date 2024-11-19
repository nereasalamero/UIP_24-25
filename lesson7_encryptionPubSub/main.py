import flet as ft
from flet.security import encrypt, decrypt

class Message:
    def __init__(self, user: str, text: str, passkey: str):
        self.user = user
        self.text = text
        self.passkey = passkey
        self.encrypted_text = encrypt(self.text, self.passkey)

def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
    page.title = "Flet Chat"
    
    # Send a message
    def send_message_click(e):
        if message.value != "":
            page.pubsub.send_all_on_topic(
                publish_to.value,
                Message(user.value, message.value, passkey.value)
            )
            print(f"Message sent: {user.value} - {message.value}")
            message.value = ""
            page.update()
    
    # Receive a message
    def on_message(topic, msg: Message):
        decrypted = decrypt(msg.encrypted_text, passkey.value)
        chat.controls.append(ft.Text(f"{msg.user}: {decrypted}"))
        print(f"Message from {msg.user}: {msg.text}")
        page.update()
    
    # Subscribe to a group
    def subscribe_on_change(e):
        page.pubsub.unsubscribe_all()
        page.pubsub.subscribe_topic(subscribe_to.value, on_message)
        print(f"Subscribed to {subscribe_to.value}")

    # Publish a message to a group
    publish_to = ft.Dropdown(
        label="Publish to",
        options=[
            ft.dropdown.Option("Group 1"),
            ft.dropdown.Option("Group 2"),
            ft.dropdown.Option("Group 3")
        ],
        width=200,
        on_change=lambda e: print(f"Publishing to {publish_to.value}")
    )

    # Subscribe to a group
    subscribe_to = ft.Dropdown(
        label="Subscribe to",
        options=[
            ft.dropdown.Option("Group 1"),
            ft.dropdown.Option("Group 2"),
            ft.dropdown.Option("Group 3")
        ],
        width=200,
        on_change=subscribe_on_change,
    )

    # Chat messages
    chat = ft.ListView(
        expand=True,
        spacing=10,
        auto_scroll=True,
    )

    user=ft.TextField(label="Username", width=150)
    passkey=ft.TextField(label="Passkey", width=150)

    # New message input
    message = ft.TextField(
        label="Message",
        expand=True,
        on_submit=send_message_click,
    )

    page.add(
        ft.Container(
            content= chat,
            border=ft.border.all(1, ft.colors.OUTLINE),
            border_radius=5,
            padding=10,
            expand=True,
        ),
        ft.Column([
            ft.Row([publish_to, subscribe_to, passkey]),
            ft.Row([user, message, ft.ElevatedButton("Send", on_click=send_message_click)])
        ])
    )


ft.app(main)
