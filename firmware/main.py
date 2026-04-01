import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.rotary_encoders import RotaryEncoder

keyboard = KMKKeyboard()

keyboard.row_pins = (board.GP0, board.GP1, board.GP2, board.GP3)
keyboard.col_pins = (board.GP4, board.GP5, board.GP6, board.GP7)

layers_ext = Layers()
keyboard.modules.append(layers_ext)

rotary = RotaryEncoder()
keyboard.modules.append(rotary)

rotary.pins = [
    (board.GP12, board.GP13, board.GP14),
    (board.GP15, board.GP16, board.GP17)
]

keyboard.keymap = [
    [
        KC.A, KC.B, KC.C, KC.D,
        KC.E, KC.F, KC.G, KC.H,
        KC.I, KC.J, KC.K, KC.L,
        KC.M, KC.N, KC.O, KC.P
    ]
]

rotary.keycode_map = [
    [KC.VOLU, KC.VOLD, KC.MUTE],
    [KC.PGUP, KC.PGDN, KC.ENTER]
]

if __name__ == "__main__":
    keyboard.go()
