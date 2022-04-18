"""This accepts an image output path, selects a random image and quote, saves the image to the output path and returns the path to the image."""

import random
from PIL import Image, ImageDraw, ImageFont

class MemeEngine:
    """This class takes in an image output path, selects a random image and quote, saves the image to the output path and returns the path to the image."""
    
    def __init__(self, output_path):
        """Create instance of class."""
        self.output_path = output_path

    @staticmethod
    def get_rand_y(value):
        """Return a random y-axis."""
        y_min = 10
        y_max = value-100
        return random.randint(y_min, y_max)

    def make_meme(self, path, text, author, width=500) -> str:
        """Create meme with provided text and author."""
        try:
            img = Image.open(path)
        except Exception as err:
            print(f'Exception: {err}')
        else:
            if width is not None:
                ratio = width/float(img.size[0])
                height = int(ratio*float(img.size[1]))
                img = img.resize((width, height), Image.NEAREST)

            if text and author:
                message = f'{text}\n- {author}'
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype("arial.ttf", 20)
                axis = (10, self.get_rand_y(img.size[1]))
                draw.text(axis, message, font=font, fill='white')

            p_path = f'{self.output_path}/{random.randint(0, 1000000)}.jpeg'

            img.save(p_path)
            print(f"Meme saved to {self.output_path}")
            return p_path