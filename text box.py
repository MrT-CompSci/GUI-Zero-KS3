from guizero import App, TextBox, PushButton, Text, Picture, alerts


def start():
    alerts.info("HAL9000", "I'm sorry " + textbox.value + " I'm afraid I can't do that")

def key_pressed(key):
    print("key pressed {}".format(key))    

app = App()

text = Text(app, text="What is your name?")

textbox = TextBox(app)

textbox.update_command(key_pressed)

picture =Picture(app, image="hal.png")

button = PushButton(app, text="Open the pod bay doors please", command=start)

app.display()
