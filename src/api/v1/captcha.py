
# Imports
from flask import request
from flask_restx import Namespace, Resource, fields
from src.captcha import TextCaptcha

# API documentation init
api = Namespace('captcha', description='Get captcha and solve it')
text_captcha = TextCaptcha()


@api.route('')
class Authentication(Resource):

    def get(self):
        """
        Get a captcha image.
        Return a captcha and its unique id.
        """

        # If a JSON is send,
        if content := request.get_json():
            print(type(text_captcha.get_captcha()))
            return content

    def post(self):
        """
        Send the captcha resolution

        Receive the resolution of the captcha and return
        a confirmation when correct.
        """

        # If a JSON is send,
        if content := request.get_json():
            return content
