from signal import pause
from gpiozero import Button
import requests

ip_addr = ""
port = 5000

button_map = {
    "GPIO6":  "1",
    "GPIO13": "2",
    "GPIO19": "3",
    "GPIO26": "4"}

def tx(button):
    angle = button_map[str(button.pin)]
    requests.post("http://%s:%s/hate5grip?angle=%s" % (ip_addr, port, angle))

button1 = Button(6)
button2 = Button(13)
button3 = Button(19)
button4 = Button(26)

try:
    button1.when_pressed = tx
    button2.when_pressed = tx
    button3.when_pressed = tx
    button4.when_pressed = tx

    pause()

finally:
    pass
