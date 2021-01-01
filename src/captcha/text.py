
from captcha.image import ImageCaptcha


class TextCaptcha:
    """A simple text captcha generator."""

    def __init__(self, width=280, height=90):

        # Create an ImageCaptcha generator
        self.generator = ImageCaptcha(width, height)

    def get_image(self):
        """Create a captcha as a .png file and return its path."""

        # TODO: Save the image into a temporary directory
        self.generator.write('hello17word', "captcha.png")

    def get_captcha(self):
        """Create a captcha and return it as io.BytesIO Object."""

        return self.generator.generate('hello17word')
