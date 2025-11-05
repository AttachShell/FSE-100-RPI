import subprocess
import base64
import openai
import os

# Create the payload for the API request
IMG_PATH = 'captured_image.jpg'


def init():
    # Set OpenAI Key
    # openai.api_key = os.getenv('OPENAI_API_KEY')

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
    
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=message,
        max_tokens=300,
    )

    # Output the result
    print(response.choices[0].message.content)


# Encode the image to Base64
def encode_image(image_path):
    with open(IMG_PATH, 'rb') as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

