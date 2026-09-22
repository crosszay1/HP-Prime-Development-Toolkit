# What is this?

This is a set of micropython apps intended for modification and to act as templates and tech demos for the HP prime g2 graphing calculator.

# Contents
- UI system featuring
  - Notification system with text wrapping
  - GUI user input system
  - Simple UI in which the user and scroll through a list of buttons, select one, which in turn runs code.
- Video system
  - Plays __video__ on the HP prime g2 graphing calculator?
  - Q: How is this possible?
    - A: This works by taking a video file, taking each frame, and putting it side by side in a png file (automated via script in scripts/). We then render a certain portion of that image on the calculator, then move to the right by a certain number of pixels. We do this many times a second, creating a fluent video.
- Keycode finder
  - Very simple app. Click a button on your calculator, and this app will tell you what the keycode is. Very useful for development!  
