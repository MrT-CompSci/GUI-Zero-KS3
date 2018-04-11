from guizero import App, TextBox, PushButton, Text, Picture, Slider, alerts

def clamp(x): 
  return max(0, min(x, 255))



def slider_changed_r(slider_value):
    textbox_r.text_color = "red"
    textbox_r.value = slider_value
    color_change()
    
    

def slider_changed_g(slider_value):
    textbox_g.text_color = "green"
    textbox_g.value = slider_value
    color_change()

def slider_changed_b(slider_value):
    textbox_b.text_color = "blue"
    textbox_b.value = slider_value
    color_change()

def color_change():
    app.bg = (int(slider_r.value), int(slider_g.value), int(slider_b.value))
    textbox_hex.value = "#{0:02x}{1:02x}{2:02x}".format(clamp(slider_r.value), clamp(slider_g.value), clamp(slider_b.value))

app = App()

text = Text(app, text="Colour Mixer")

textbox_r = TextBox(app, text = "0")
textbox_g = TextBox(app, text = "0")
textbox_b = TextBox(app, text = "0")

textbox_hex=TextBox(app)

slider_r = Slider(app,  end = 255, command = slider_changed_r)
slider_g = Slider(app, end = 255,   command = slider_changed_g)
slider_b = Slider(app, end = 255,  command = slider_changed_b)



app.display()
