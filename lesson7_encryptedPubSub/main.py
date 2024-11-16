import flet as ft
from flet.security import encrypt, decrypt


# Class to represent a message
class Message():
    def __init__(self, user: str, text: str, passkey: str):
        self.user = user
        self.text = text
        self.passkey = passkey
        self.encrypted_text = encrypt(self.text, self.passkey)
        self.decrypted_text = decrypt(self.encrypted_text, self.passkey)

def main(page: ft.Page):
    page.title = "Flet Chat"
    
    publish_to = ft.Dropdown(
        label="Publish to",
        options=[
            ft.dropdown.Option("Group 1"),
            ft.dropdown.Option("Group 2"),
            ft.dropdown.Option("Group 3")
        ],
        width=200,
    )
    subscribe_to = ft.Dropdown(
        label="Subscribe to",
        options=[
            ft.dropdown.Option("Group 1"),
            ft.dropdown.Option("Group 2"),
            ft.dropdown.Option("Group 3")
        ],
        width=200,
        # on_change=lambda e: subscribe_topic
    )
    
    # subscribe to broadcast messages
    def on_message(topic, msg: Message, e):
        print(f"Messages: {messages.controls}")
        decrypted = decrypt(msg.encrypted_text, passkey.value)
        messages.controls.append(ft.Text(f"{msg.user}: {decrypted}"))
        print(f"Received message from {msg.user}: {msg.text} // {decrypted}")
        page.update()

    def subscribe_topic(e):
        topic = subscribe_to.value
        page.pubsub.subscribe_topic(topic, on_message)
        print(f"Subscribed to {topic}")
        print(f"Messages: {messages.controls}")
        page.update()
    
    topic = subscribe_to.value
    page.pubsub.subscribe_topic(topic, on_message)
    #page.pubsub.subscribe(on_message)

    def send_click(e):
        new_msg = Message(user.value, message.value, passkey.value)
        publish = publish_to.value
        page.pubsub.send_all_on_topic(publish, new_msg)
        print(f"Sent message to {publish}")
        print(f"Message: {new_msg.text}")
        #page.pubsub.send_all(new_msg)
        # clean up the form
        message.value = ""
        page.update()
    
    messages = ft.Column()
    user = ft.TextField(label="Username", width=150)
    message = ft.TextField(label="Message", expand=True, on_submit=send_click)
    passkey = ft.TextField(label="Passkey", width=150, password=True)
    send = ft.ElevatedButton("Send", on_click=send_click)
    #subscribe = ft.ElevatedButton("Subscribe", on_click=subscribe_topic)
    page.add(
        ft.Column([
            # Add the messages column to the page
            messages,
            # Add the dropdowns and the passkey field to the page
            ft.Row(controls=[publish_to, subscribe_to, passkey]),        
            # Add the user input fields and the send button to the page
            ft.Row(controls=[user, message, send]),
            # ft.Row(controls=[subscribe])
        ])
    )
    page.update()

ft.app(target=main)