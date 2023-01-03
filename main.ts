input.onGesture(Gesture.ScreenUp, function on_gesture_screen_up() {
    basic.showNumber(Step_Count)
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    Step_Count = 0
    basic.clearScreen()
    basic.showIcon(IconNames.No)
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
    Step_Count += 1
})
let Step_Count = 0
Step_Count = 0
