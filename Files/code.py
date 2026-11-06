print("Starting")
import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC, make_key
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.rgb import RGB
from kmk.extensions.rgb import AnimationModes
from kmk.modules.combos import Combos, Chord, Sequence

keyboard = KMKKeyboard()
combos = Combos()
KMKKeyboard.modules.append(combos)

#Defining MCU GPIO pins
COL1 = board.IO6
COL2 = board.IO7
COL3 = board.IO8
COL4 = board.IO10
COL5 = board.IO14
COL6 = board.IO15
ROW1 = board.IO0
ROW2 = board.IO1
ROW3 = board.IO2
ROW4 = board.IO3
ROW5 = board.IO4
MUTE = board.IO9
ENC_A = board.IO26
ENC_B = board.IO27
LED = board.IO5

#Defining the matrix dimensions and diode direction
keyboard.col_pins = (COL1,COL2,COL3,COL4,COL5,COL6)
keyboard.row_pins = (ROW1,ROW2,ROW3,ROW4,ROW5)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

#Defining the keymap
keyboard.keymap = [
    [KC.ESC, KC.KP_1, KC.KP_2,KC.KP_3,KC.KP_4,KC.Y,
     KC.TAB, KC.Q, KC.W,KC.E,KC.R,KC.T,
     KC.CAPSLOCK,KC.A,KC.S,KC.D,KC.F,KC.B,
     KC.BSLASH,KC.Z,KC.X,KC.C,KC.V,KC.NO,
     KC.LSHIFT,KC.LCTRL,KC.LALT,KC.NO ,KC.SPACE,KC.NO,
    ]
]

#Defining the combos
combos.combos = [
    Chord((25, 7), KC.RGB_MOD),
    Chord((25, 0), KC.RGB_TOG),
]

#Defining encoder functions
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
encoder_handler.pins = ((ENC_A, ENC_B, MUTE, False),)
encoder_handler.map = (((KC.VOLD, KC.VOLU, KC.MUTE),),)

#Defining RBG patterns
rgb_ext = RGB(
    pixel_pin = LED,
    num_pixels = 6,
    val_limit = 100,
    val_default = 75,
    animation_speed = 1,
    animation_mode = AnimationModes.KNIGHT,
    refresh_rate = 50,
)
keyboard.extensions.append(rgb_ext)


if __name__ == '__main__':
    keyboard.go()
