import subprocess
import base64
from openai import OpenAI
import os
import RPi.GPIO as GPIO
from dotenv import load_dotenv

load_dotenv()

# Create the payload for the API request
IMG_PATH = 'captured_image.jpg'
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def init(pin):
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(pin, GPIO.BOTH, callback=callback, bouncetime=200)
    print("INITIALIZING...")

def callback(chn):
    run()

def run():
    # Capture the image using fswebcam
    subprocess.run(['fswebcam', '-r', '1280x720', '--no-banner', IMG_PATH])
    base64_image = encode_image(IMG_PATH)

    message = [
    {
        "role": "user",
        "content": [
            {"type": "text", "text": "How far is the closest object in this image?"},
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}},
        ],
      }
    ]
    
    response = client.chat.completions.create(
        model="gpt-5-nano",
        messages=message,
        max_completion_tokens=300,
    )

    # Output the result
    print(response.choices[0].message.content)

# Encode the image to Base64
def encode_image(image_path):
    with open(IMG_PATH, 'rb') as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

