def on_gesture_screen_up():
    basic.show_number(Step_Count)
input.on_gesture(Gesture.SCREEN_UP, on_gesture_screen_up)

def on_button_pressed_ab():
    global Step_Count
    Step_Count = 0
    basic.clear_screen()
    basic.show_icon(IconNames.NO)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_gesture_shake():
    global Step_Count
    Step_Count += 1
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

Step_Count = 0
Step_Count = 0