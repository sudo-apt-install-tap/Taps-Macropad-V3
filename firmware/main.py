import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.rotary_encoders import RotaryEncoder

keyboard = KMKKeyboard()

# ===== ROWS & COLUMNS =====
keyboard.row_pins = (board.GP0, board.GP1, board.GP2, board.GP3)  # ROW0-ROW3
keyboard.col_pins = (board.GP4, board.GP5, board.GP6, board.GP7)  # COL0-COL3

# ===== MODULES =====
layers_ext = Layers()
keyboard.modules.append(layers_ext)

rotary = RotaryEncoder()
keyboard.modules.append(rotary)

# ===== ROTARY ENCODERS =====
# Rotary Encoder 1 (left)
rotary.pins = [
    (board.GP12, board.GP13, board.GP14),  # A, B, Switch
    (board.GP15, board.GP16, board.GP17)   # A, B, Switch
]

# ===== KEYMAP =====
# 4x4 buttons + 2 encoder switches (last 2 keys)
keyboard.keymap = [
    [  # Base layer
        KC.A, KC.B, KC.C, KC.D,
        KC.E, KC.F, KC.G, KC.H,
        KC.I, KC.J, KC.K, KC.L,
        KC.M, KC.N, KC.O, KC.P
    ]
]

# ===== ENCODER FUNCTIONS =====
rotary.keycode_map = [
    [KC.VOLU, KC.VOLD, KC.MUTE],   # Encoder 1 CW, CCW, Press
    [KC.PGUP, KC.PGDN, KC.ENTER]   # Encoder 2 CW, CCW, Press
]

if __name__ == "__main__":
    keyboard.go()
