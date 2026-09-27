# mbot2.py
# PyCharm-only shim so `import mbot2` gives real autocompletion.
# NEVER upload this file. The script you paste into mBlock must
# contain only: import cyberpi / import mbot2 / import event / import time
from cyberpi import mbot2 as _m

servo_set      = _m.servo_set
servo_add      = _m.servo_add
servo_get      = _m.servo_get
servo_release  = _m.servo_release
servo_drive    = _m.servo_drive
motor_add      = _m.motor_add
motor_set      = _m.motor_set
motor_stop     = _m.motor_stop