# Import the Python standard libraries needed to run the code
import os
# from os.path import exists
import random

# Import the third-party libraries needed to run the code
from PIL import Image
import requests
from twython import Twython

# Pass the environment variables into Twython to be used to authenticate into Twitter and tweet
twitter = Twython(
    os.environ.get("APP_KEY"),
    os.environ.get("APP_SECRET"),
    os.environ.get("OAUTH_TOKEN"),
    os.environ.get("OAUTH_TOKEN_SECRET"),
)

def main():   
    # Create the URL for the random image and set the image download path
    file_number = random.randrange(1, 278)
    file_url = "https://source.unsplash.com/collection/2489501/" + str(file_number) + "/"
    file_path = str(file_number) + '.' + 'jpg'
    # file_path = 'photos/' + str(file_number) + '.' + 'jpg'

    # Use the Requests library to download and close the file
    response = requests.get(file_url)
    file = open(file_path, 'wb')
    file.write(response.content)
    file.close()

    # Open the image using the Pillow library
    new_image = Image.open(file_path)

    # Show the image before the transformation
    new_image.show()

    # Randomly choose an image filter algorithm from a list and call its function to apply the filter to the image
    choices = [no_change, black_and_white_algorithm, sepia_algorithm, negative_algorithm]
    algorithm = random.choice(choices)(new_image, file_path)
    
    # Open the modified image
    modified_image = open(file_path, 'rb')

    # Use Twython library to upload and tweet the modified image, optionally with a `status` message
    response = twitter.upload_media(media=modified_image, media_type='image', media_category='tweet_image')
    twitter.update_status(status='', media_ids=[response['media_id']])

    # Call the `remove_file()` function to delete the image
    remove_file(file_path)
 
# Return original file, no algorithm applied
def no_change(new_image, file_path):
    modified_image = new_image
    save_image(modified_image, file_path)

# Apply the "Black and White" Algorithm
def black_and_white_algorithm(new_image, file_path):
    modified_image = new_image.convert('L')
    save_image(modified_image, file_path)

# Apply the "Sepia" Algorithm
def sepia_algorithm(new_image, file_path):

    width, height = new_image.size
    sepia_image = Image.new("RGB",(width, height))
    raw_pixels = new_image.load()
    sepia_pixels = sepia_image.load()

    for y in range(height):
        for x in range(width):
            R,G,B = raw_pixels[x,y]
            oR = (R*.393) + (G*.769) + (B*.189)
            oG = (R*.349) + (G*.686) + (B*.168)
            oB = (R*.272) + (G*.534) + (B*.131)
            sepia_pixels[x,y] = (int(oR),int(oG),int(oB))

    modified_image = sepia_image
    save_image(modified_image, file_path)

# Apply the "Negative" Algorithm
def negative_algorithm(new_image, file_path):

    width, height = new_image.size
    negative_image = Image.new("RGB",(width, height))
    raw_pixels = new_image.load()
    negative_pixels = negative_image.load()

    for y in range(height):
        for x in range(width):
            R,G,B = raw_pixels[x,y]
            oR = (R*.393) + (G*.769) + (B*.189)
            oG = (R*.349) + (G*.686) + (B*.168)
            oB = (R*.272) + (G*.534) + (B*.131)
            negative_pixels[x,y] = (255-R,255-G,255-B)

    modified_image = negative_image
    save_image(modified_image, file_path)
    
# Apply the "Blue" Algorithm
def blue_algorithm(new_image):

    save_image(modified_image, file_path)

# Apply the "Red" Algorithm
def red_algorithm(new_image):

    save_image(modified_image, file_path)

# Save modified image and return; optionally, show the image after the transformation
def save_image(modified_image, file_path):
    modified_image.show()
    modified_image.save(file_path)
    return modified_image

# If file exists, remove file
def remove_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)

if __name__ == "__main__": 
    main() 
