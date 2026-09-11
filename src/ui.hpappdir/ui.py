from math import *

from hpprime import *
from uio import *
from urandom import *

selected = 0
top = 0


class UI:
  INPUT_VAR = "PyInputStr"

  @staticmethod
  def getinput(message="", title="Input", default=""): # Abstraction for getting user input
    while eval('getkey') != -1:
      pass
    eval(UI.INPUT_VAR + ':="' + str(default) + '"')
    ok = eval('INPUT(' + UI.INPUT_VAR + ',"' + str(title) + '","' + str(message) + '","ENTER to confirm, ESC to cancel")')

    if not ok:
      return default

    return eval(UI.INPUT_VAR)

  @staticmethod
  def sendNotification(message: str): # Sends notifcations. 
      while eval('getkey') != -1: #Wait till enter is released or we'll immediately close the popup
        pass

      # Wrap text
      max_chars = 25 # Guesstimated this.
      words = message.split(" ")
      lines = []
      line = ""

      for word in words:
        if len(line) + len(word) + 1 <= max_chars:
          if line:
            line += " "
          line += word
        else:
          lines.append(line)
          line = word

      if line:
        lines.append(line)

      # Calculate popup height
      line_height = 15
      box_height = 45 + (len(lines) * line_height)

      # Draw the popup background
      # fillrect(grob, x, y, width, height, edge_color, fill_color)
      fillrect(1, 60, 90, 200, box_height, 0x000000, 0xEEEEEE)
      
      # Write text
      y = 100

      for line in lines:
        eval('textout_p("' + str(line) + '",G1,75,' + str(y) + ',4,#000000)')
        y += line_height

      eval('textout_p("Press any key to dismiss",G1,75,' + str(y + 5) + ',2,#555555)')
      
      #Push the buffer to the screen
      blit(0, 0, 0, 1)

      # Close when use presses a key
      while eval('getkey') == -1:
        pass


  @staticmethod
  def draw_menu(VISIBLE, MENU):

    # Clear screen
    dimgrob(1, 320, 240, 0xFFFFFF)

    # Draw title and current time (HP Prime Time is HH.MMSS)
    eval('textout_p("Dev Menu",G1,10,8,6,#000000)')

    time = eval("Time")
    hours = int(time)
    minutes_float = (time - hours) * 60
    minutes = int(minutes_float)
    seconds = int((minutes_float - minutes) * 60 + 0.5)

    if seconds >= 60:
        seconds = 0
        minutes += 1

    if minutes >= 60:
        minutes = 0
        hours = (hours + 1) % 24

    h_str = str(hours) if hours >= 10 else "0" + str(hours)
    m_str = str(minutes) if minutes >= 10 else "0" + str(minutes)
    s_str = str(seconds) if seconds >= 10 else "0" + str(seconds)
    eval('textout_p("' + h_str + ":" + m_str + ":" + s_str + '",G1,130,12,4,#000000)')

    # Draw menu items
    for i in range(VISIBLE):
      index = top + i

      if index >= len(MENU):
        break

      y = 30 + i * 20 # Difference in y position for each item
      item = MENU[index]

      # Highlight selected item
      if index == selected:
        fillrect(1, 5, y - 2, 310, 22, 0xCCCCCC, 0xCCCCCC)
        eval(
          'textout_p(">' + str(item.display) + '",G1,15,' + str(y) + ',4,#000000)'
        )
      else:
        eval(
          'textout_p("' + str(item.display) + '",G1,25,' + str(y) + ',4,#000000)'
        )

    # Simple scroll indicators
    if top > 0:
      eval('textout_p("^",G1,305,35,3,#000000)')

    if top + VISIBLE < len(MENU):
      eval('textout_p("v",G1,305,225,3,#000000)')

    blit(0, 0, 0, 1)