def on_gesture_shake():
    global 步數
    步數 += 1
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_gesture_screen_up():
    basic.show_number(步數)
input.on_gesture(Gesture.SCREEN_UP, on_gesture_screen_up)

def on_button_pressed_ab():
    global 步數
    步數 = 0
    basic.clear_screen()
    basic.show_icon(IconNames.NO)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

步數 = 0
步數 = 0