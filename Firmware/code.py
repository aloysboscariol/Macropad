import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC

keyboard = KMKKeyboard()

PINS = [
    board.GP7,
    board.GP1,
    board.GP2,
    board.GP4,
    board.GP3,
    board.GP6,
]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [
        KC.F13,
        KC.F14,
        KC.F15,
        KC.F16,
        KC.F17,
        KC.F18,
    ]
]

if __name__ == "__main__":
    keyboard.go()
