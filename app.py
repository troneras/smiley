from fastapi import FastAPI, File, UploadFile
from PIL import Image
import numpy as np
import io
from PIL import Image
import numpy as np


def convert_image_to_ascii(img_path, new_width=100):
    # Load the image from file
    img = Image.open(img_path)

    # Define the ASCII characters to use
    ascii_chars = "@%#*+=-:. "

    # Resize the image according to a new width
    width, height = img.size
    ratio = height / width
    new_height = int(new_width * ratio)
    img = img.resize((new_width, new_height))

    # Convert image to grayscale
    img = img.convert("L")

    # Convert grayscale image to numpy array
    img_data = np.array(img)

    # Normalize data to match the ASCII characters
    img_data = (img_data / 255) * (len(ascii_chars) - 1)

    # Map each pixel to an ASCII char and create the ASCII art
    ascii_img = "\n".join("".join(ascii_chars[int(pixel)] for pixel in row) for row in img_data)

    # Return the ASCII art
    return ascii_img

# Example usage
# img_path = 'Smiley.png'
# ascii_art = convert_image_to_ascii(img_path, 40)
# print(ascii_art)


# exit(0)

app = FastAPI()

@app.post("/convert-to-ascii/")
async def convert_to_ascii(file: UploadFile = File(...), size: int = 100):
    """
    Convert an uploaded image file to ASCII art.

    Parameters:
    - file: UploadFile object representing the uploaded image file.
    - size: Desired width of the ASCII art (default is 100).

    Returns:
    - Dictionary containing the ASCII art as a string.
    """
    content = await file.read()
    image_stream = io.BytesIO(content)
    ascii_art = convert_image_to_ascii(image_stream, size)
    return {"ascii_art": ascii_art}
