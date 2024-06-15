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

# graphics = None
# WIDTH = None
# HEIGHT = None

graphics = PicoGraphics(DISPLAY)
WIDTH, HEIGHT = graphics.get_bounds()
graphics.set_font("serif")

FILENAME = "display_image.jpg"

API_URL = "https://i.imgur.com"

UPDATE_INTERVAL_MINUTES = 1


def update():
    image_url = API_URL + "/Vnfuid9.jpg"

    # Grab the data
    # socket = urequest.urlopen(API_URL)
    # gc.collect()
    # j = load(socket)
    # socket.close()
    # apod_title = j['title']
    # gc.collect()

    # Grab the image
    socket = urequest.urlopen(image_url)

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


def draw():
    jpeg = jpegdec.JPEG(graphics)
    gc.collect()  # For good measure...

    graphics.set_pen(1)
    graphics.clear()

    jpeg.open_file(FILENAME)
    jpeg.decode()

    gc.collect()

    graphics.update()


while True:
    update()
    draw()
    ih.sleep(UPDATE_INTERVAL_MINUTES)


