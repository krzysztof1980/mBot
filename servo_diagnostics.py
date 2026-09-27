import event, cyberpi, mbot2
import time

ARM = "S4" # 90 - level, lowest: 155, highest: 70
HAND = "S3" # 90 - parallel, narrowest w/o touching: 140

@event.is_press('middle')
def is_joy_press():
    mbot2.servo_set(90, "all")
    print_current_servo_angle("Hand: " + HAND)
    print_current_servo_angle("Arm: " + ARM)
    time.sleep(5)
    cyberpi.console.clear()

@event.is_press('up')
def is_joy_press_up():
    mbot2.servo_add(10, ARM)
    print_current_servo_angle(ARM)

@event.is_press('down')
def is_joy_press_down():
    mbot2.servo_add(-10, ARM)
    print_current_servo_angle(ARM)

@event.is_press('left')
def is_joy_press_left():
    mbot2.servo_add(-10, HAND)
    print_current_servo_angle(HAND)

@event.is_press('right')
def is_joy_press_right():
    mbot2.servo_add(10, HAND)
    print_current_servo_angle(HAND)

def print_current_servo_angle(servo):
    cyberpi.console.clear()
    cyberpi.console.println(mbot2.servo_get(servo))