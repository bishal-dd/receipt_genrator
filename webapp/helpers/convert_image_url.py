import base64


def convert_image(image):
    image = base64.b64encode(image.read()).decode('utf-8')
    return image
