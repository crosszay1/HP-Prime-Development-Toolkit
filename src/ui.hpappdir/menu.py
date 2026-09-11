from math import *

import ui
from hpprime import *
from ui import UI
from uio import *
from urandom import *

class MenuItem:
  def __init__(self, name, display, script):
    self.name = name
    self.display = display
    self.script = script


def input_test():
  UI.getinput("This is a test of the input box. Type something and press Enter.", "Input Test", "Default text")
  sendNotification("Input test completed. You typed: " + eval(UI.INPUT_VAR)) # TODO: Fix text overflowing


def notif_test():
  sendNotification("Notification test selected")


MENU = [
  MenuItem("input_test", "Input test", input_test),
  MenuItem("notif_test", "Notification test", notif_test),
]

VISIBLE = 10 # Number of items visible at once


draw_menu = UI.draw_menu
getinput = UI.getinput
sendNotification = UI.sendNotification

def run_script(number):
  #print(f"Selected: {number}") # Are f strings genuinally not supported :/
  sendNotification("You selected" + str(number))


dimgrob(1, 320, 240, 0xFFFFFF) # Create the weird graphics buffer

# Clear any previously pressed keys
while eval('getkey') != -1:
  pass


while True:
  try:
    draw_menu(VISIBLE=VISIBLE, MENU=MENU)

    # Poll for a key for up to ~1s so the clock refreshes once per second
    key = -1
    for _ in range(20):
      key = eval('getkey')
      if key != -1:
        break
      eval('wait(0.05)')

    if key == -1:
      continue

    # UP
    if key == 2:
      if ui.selected > 0:
        ui.selected -= 1

        # Scroll upward
        ui.top = min(ui.top, ui.selected)

    # DOWN
    elif key == 12:
      if ui.selected < len(MENU) - 1:
        ui.selected += 1

        # Scroll downward
        if ui.selected >= ui.top + VISIBLE:
          ui.top = ui.selected - VISIBLE + 1

    # SELECT / CENTER
    elif key == 30:
      MENU[ui.selected].script()

    # Wait for key release
    while eval('getkey') != -1:
      pass
  except KeyboardInterrupt:
    print("Alright, goodbye!")
    break #Gracefully exit without throwing an error