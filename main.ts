input.onGesture(Gesture.ScreenUp, function () {
    basic.showNumber(Step_Count)
})
input.onButtonPressed(Button.AB, function () {
    Step_Count = 0
    basic.clearScreen()
    basic.showIcon(IconNames.No)
})
input.onGesture(Gesture.Shake, function () {
    Step_Count += 1
})
let Step_Count = 0
Step_Count = 0
