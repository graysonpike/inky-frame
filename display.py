import gc
import jpegdec
from urllib import urequest
from ujson import load
from picographics import PicoGraphics, DISPLAY_INKY_FRAME_7 as DISPLAY
import inky_helper as ih

gc.collect()

try:
    from secrets import WIFI_SSID, WIFI_PASSWORD
    ih.network_connect(WIFI_SSID, WIFI_PASSWORD)
except ImportError:
    print("Create secrets.py with your WiFi credentials")
gc.collect()

graphics = None
WIDTH = None
HEIGHT = None

graphics = PicoGraphics(DISPLAY)
WIDTH, HEIGHT = graphics.get_bounds()
graphics.set_font("serif")

FILENAME = "nasa-apod-daily-2.jpg"

# A Demo Key is used in this example and is IP rate limited. You can get your own API Key from https://api.nasa.gov/
API_URL = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

# Length of time between updates in minutes.
# Frequent updates will reduce battery life!
UPDATE_INTERVAL = 240

# Variable for storing the NASA APOD Title
apod_title = None


def show_error(text):
    graphics.set_pen(4)
    graphics.rectangle(0, 10, WIDTH, 35)
    graphics.set_pen(1)
    graphics.text(text, 5, 16, 400, 2)


def update():
    global apod_title

    if True:
        # Image for Inky Frame 5.7
        IMG_URL = "https://i.imgur.com/Vnfuid9.jpg"
    elif HEIGHT == 400:
        # Image for Inky Frame 4.0
        IMG_URL = "https://pimoroni.github.io/feed2image/nasa-apod-640x400-daily.jpg"
    elif HEIGHT == 480:
        IMG_URL = "https://pimoroni.github.io/feed2image/nasa-apod-800x480-daily.jpg"

    try:
        # Grab the data
        socket = urequest.urlopen(API_URL)
        gc.collect()
        j = load(socket)
        socket.close()
        apod_title = j['title']
        gc.collect()
    except OSError as e:
        print(e)
        apod_title = "Image Title Unavailable"

    try:
        # Grab the image
        print(f"Getting image URL: {IMG_URL}")
        socket = urequest.urlopen(IMG_URL)

        gc.collect()

        data = bytearray(1024)
        print("Writing data to file from socket...")
        with open(FILENAME, "wb") as f:
            while True:
                if socket.readinto(data) == 0:
                    break
                f.write(data)
                print(".", end="")
        socket.close()
        del data
        gc.collect()
    except OSError as e:
        print(e)
        show_error("Unable to download image")


def draw():
    jpeg = jpegdec.JPEG(graphics)
    gc.collect()  # For good measure...

    graphics.set_pen(1)
    graphics.clear()

    jpeg.open_file(FILENAME)
    jpeg.decode()

    gc.collect()

    graphics.update()

update()
draw()


