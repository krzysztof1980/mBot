# event.py
# PyCharm-only shim so `import event` resolves to the real CyberPi
# event system. NEVER upload this file.
from cyberpi import event as _event

start = _event.start
is_press = _event.is_press
greater_than = _event.greater_than
smaller_than = _event.smaller_than
is_shake = _event.is_shake
is_tiltback = _event.is_tiltback
is_tiltforward = _event.is_tiltforward
is_tiltleft = _event.is_tiltleft
is_tiltright = _event.is_tiltright
is_faceup = _event.is_faceup
is_facedown = _event.is_facedown
is_clockwise = _event.is_clockwise
is_anticlockwise = _event.is_anticlockwise
is_freefall = _event.is_freefall
wifi_broadcast = _event.wifi_broadcast