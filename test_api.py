import requests

""""
POST
/convert-to-ascii/
Convert To Ascii

Convert an uploaded image file to ASCII art.

Parameters:

file: UploadFile object representing the uploaded image file.
size: Desired width of the ASCII art (default is 100).
Returns:

Dictionary containing the ASCII art as a string.
"""

def send_image_to_api(image_path, size, endpoint):
    # Define the URL
    url = endpoint + '/convert-to-ascii/'

    # Define the file data to send
    file_data = {
        'file': open(image_path, 'rb'),
    }

    # Define the parameters to send
    params = {
        'size': size
    }

    # Send the request
    response = requests.post(url, files=file_data, params=params)

    # Check the response
    if response.status_code == 200:
        return response.json()['ascii_art']
    else:
        return 'Failed to send image'

# Use the function
print(send_image_to_api('Smiley.png', 10, 'http://localhost:8000'))
