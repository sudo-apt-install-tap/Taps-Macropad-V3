import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()

# MATRIX
keyboard.col_pins = (
    board.GP29,
    board.GP28,
    board.GP27,
    board.GP26,  
)

keyboard.row_pins = (
    board.GP15,
    board.GP14,
    board.GP13,
    board.GP12,
)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

# MEDIA KEYS
media = MediaKeys()
keyboard.extensions.append(media)

# ENCODERS
encoder_handler = EncoderHandler()

encoder_handler.pins = (
    (board.GP10, board.GP11, None, False),  # Encoder 1
    (board.GP7, board.GP8, None, False),   # Encoder 2
)

encoder_handler.map = [
    [
        (
            KC.AUDIO_VOL_DOWN,
            KC.AUDIO_VOL_UP,
        ),

        (
            KC.LSFT(KC.LALT(KC.TAB)),
            KC.LALT(KC.TAB),
        ),
    ]
]

keyboard.modules.append(encoder_handler)

# KEYMAP
keyboard.keymap = [
    [
        KC.ESC,   KC.Q,     KC.W,     KC.E,
        KC.A,     KC.S,     KC.D,     KC.F,
        KC.Z,     KC.X,     KC.C,     KC.V,
        KC.TAB,   KC.SPC,   KC.BSPC,  KC.ENT,
    ]
]

if __name__ == '__main__':
    keyboard.go()
