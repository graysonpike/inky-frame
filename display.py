from time import sleep
from picographics import PicoGraphics, DISPLAY_INKY_FRAME_7 as DISPLAY


# Sleep to allow USB to initialize
sleep(0.5)


COLOR_WHITE = 1
COLOR_BLACK = 0
Y_OFFSET = 35


class Display:
    
    def __init__(self):
        self.graphics = None
        self.font_scale = 2
        self.init_graphics()

    def init_graphics(self):
        self.graphics = PicoGraphics(DISPLAY)
        self.width, self.height = self.graphics.get_bounds()
        self.graphics.set_font("bitmap8")


    def clear(self, color):
        """
        Fill the display with the given color.
        """
        self.graphics.set_pen(color)
        self.graphics.clear()


    def demo_hello_world(self):
        """
        Display a hello world message.
        """
        self.clear(COLOR_WHITE)
        self.graphics.set_pen(COLOR_BLACK)
        #self.graphics.set_thickness(2)
        self.graphics.text("Hello World", 0, 0 + Y_OFFSET, scale=self.font_scale)
        self.graphics.update()
    
    
    def demo_word_repeat(self, word):
        """
        Artfully repeat a word across the screen with a horizontal offset on
        each row to create a staggered effect.
        """
        # Clear the screen and set a white background
        self.clear(COLOR_WHITE)
        # Set the text color to black
        self.graphics.set_pen(COLOR_BLACK)
        # Define spacing between words
        word_width = self.graphics.measure_text(word, self.font_scale)
        spacing = 20
        vertical_spacing = (8 * self.font_scale) + spacing
        horizontal_offset_increment = word_width // 2
        # Calculate number of words per row and number of rows, adding a few extra 
        # for both to ensure that applying our horizontal offset doesn't leave 
        # any part of the screen blank
        words_per_row = (self.width // (word_width + spacing)) + 10
        num_rows = self.height // vertical_spacing + 10
        # Draw words to screen
        for row in range(num_rows):
            for col in range(words_per_row):
                self.graphics.text(
                    word,
                    col * (word_width + spacing) - (horizontal_offset_increment * row),
                    row * vertical_spacing,
                    scale=self.font_scale
                )
        self.graphics.update()
        

display = Display()
display.demo_word_repeat("devika")
#display.demo_hello_world()

