def pulsador_nombre():
    basic.show_string("Mi nombre es Vanessa")

def pulsador_edad():
    basic.show_string("Mi edad es 15")

input.on_button_pressed(Button.A, pulsador_nombre)
input.on_button_pressed(Button.B, pulsador_edad)
