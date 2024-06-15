import gc
import time
from machine import reset
import inky_helper as ih

# Uncomment the line for your Inky Frame display size
# from picographics import PicoGraphics, DISPLAY_INKY_FRAME_4 as DISPLAY  # 4.0"
# from picographics import PicoGraphics, DISPLAY_INKY_FRAME as DISPLAY      # 5.7"
from picographics import PicoGraphics, DISPLAY_INKY_FRAME_7 as DISPLAY  # 7.3"

# Create a secrets.py with your Wifi details to be able to get the time
#
# secrets.py should contain:
# WIFI_SSID = "Your WiFi SSID"
# WIFI_PASSWORD = "Your WiFi password"

# A short delay to give USB chance to initialise
time.sleep(0.5)

# Setup for the display.
graphics = PicoGraphics(DISPLAY)
WIDTH, HEIGHT = graphics.get_bounds()
graphics.set_font("serif")

ih.launch_app("display_picture.py")

# Pass the graphics object from the launcher to the app
ih.app.graphics = graphics
ih.app.WIDTH = WIDTH
ih.app.HEIGHT = HEIGHT
