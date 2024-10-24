"""Module to generate meme."""

import os
import textwrap
from random import randint

from PIL import Image, ImageDraw, ImageFont


class MemeEngine:
    """A meme generator."""

    allowed_extensions = ["jpg", "png"]

    def __init__(
        self,
        output_dir: str,
        text_font_path="./_data/fonts/Blinker-Regular.ttf",
        author_font_path="./_data/fonts/Blinker-Regular.ttf",
    ):
        """
        Create a new 'MemeEngine'.

        :param output_dir: Path to the directory memes are saved to.
        :param text_font_path: Path of the font file of quote's.
        :param author_font_path: Path of the font file of an author's name.
        """
        self.output_dir = output_dir
        self.text_font_path = text_font_path
        self.author_font_path = author_font_path

    def make_meme(
        self,
        img_path: str,
        text: str,
        author: str,
        width: int = 500,
        text_font_size: int = 32,
        author_font_size: int = 20,
    ) -> str:
        """Generate a new meme.

        param img_path: Path to the base image.
        param text: Body of the quote.
        param author: Author of the quote.
        param width: Width of the meme in pixels.
        param text_font_size: Font size of the body of the quote.
        param author_font_size: Font size of the author's name.
        return: Path to the created meme.
        """
        # Check file type
        file_extension = img_path.split(".")[-1].lower()
        if file_extension not in self.allowed_extensions:
            allowed_types = ", ".join(self.allowed_extensions)
            raise ValueError(
                f"Unable to open {img_path}. Allowed file types:"
                f"{allowed_types}."
            )

        with Image.open(img_path) as image:
            # resize
            image = self.resize_image(image, width)

            # add quote
            self.add_quote(image, text, author, text_font_size,
                           author_font_size)

            # save
            out_path = os.path.join(
                self.output_dir,
                f"meme_{randint(0, 10000)}.{file_extension}",
            )
            image.save(out_path)
        return out_path

    @staticmethod
    def resize_image(image: Image.Image, width: int) -> Image.Image:
        """Resize an image maintaining its aspect ratio.

        :param image: Image.
        :param width: Target width in pixels.s
        :return: Resized image.
        """
        orig_width, orig_height = image.size
        height = round(width / orig_width * orig_height)
        return image.resize((width, height))

    def add_quote(
        self,
        image: Image.Image,
        text: str,
        author: str,
        text_font_size: int = 32,
        author_font_size: int = 20,
        gap: int = 10,
    ):
        """Add a quote to an image.

        :param image: Image
        :param text: Body of the quote
        :param author: Author of the quote
        :param text_font_size: Font size of the body of the quote
        :param author_font_size: Font size of the author's name
        :param gap: Gap between body and author text
        """
        width, height = image.size

        # create fonts
        text_font = ImageFont.truetype(self.text_font_path, text_font_size)
        author_font = ImageFont.truetype(self.author_font_path,
                                         author_font_size)

        # create an object for drawing on the image
        d = ImageDraw.Draw(image)

        # create mask of text and author
        text_mask = text_font.getmask(text)
        author_mask = author_font.getmask(author)

        # get size of text and author
        text_length, text_height = text_mask.size
        author_length, author_height = author_mask.size
        extra_padding = 0

        # wrap text if it is too long
        if text_length >= 0.8 * width:
            pixels_per_char = text_length / len(text)
            max_line_length = round(width * 0.8 / pixels_per_char)
            text = textwrap.fill(text, max_line_length)
            text_mask = text_font.getmask(text)
            text_length, text_height = text_mask.size
            extra_padding = round(text_font_size * 0.4)

        # randomly select position of text
        max_text_x = width - text_length
        text_x = randint(0, max_text_x) if max_text_x > 0 else 0
        text_y = randint(
            0,
            max(
                0,
                height - text_height - author_height - gap - extra_padding,
            ),
        )
        author_y = text_y + text_height + gap

        # add body of quote
        d.text(
            (text_x, text_y),
            text,
            (0, 0, 0),
            font=text_font,
            stroke_width=2,
            stroke_fill=(255, 255, 255),
        )

        # add author
        author = 4 * " " + "- " + author
        d.text(
            (text_x, author_y),
            author,
            (0, 0, 0),
            font=author_font,
            stroke_width=1,
            stroke_fill=(255, 255, 255),
        )
