import sys
from promptAssistant import get_prompt_response
from generateImage import generate_image
from PIL import Image
import os


def get_unique_path(base_path):
    directory = os.path.dirname(base_path)
    filename = os.path.basename(base_path)
    name, ext = os.path.splitext(filename)

    # Remove any existing numbers from name
    base_name = name.split("-")[0]

    counter = 1
    while True:
        new_path = os.path.join(directory, f"{base_name}-{counter:03d}{ext}")
        if not os.path.exists(new_path):
            return new_path
        counter += 1


def main(user_prompt: str, output_path: str = "output/genmoji.png"):
    # Get the response from the prompt assistant
    prompt_response = get_prompt_response(user_prompt)
    print("Prompt Created: " + prompt_response)

    # Generate the image using the response from the prompt assistant
    image = generate_image(prompt_response)

    width, height = image.size
    newImg = image.resize((width * 5, height * 5), Image.LANCZOS)

    output_path = get_unique_path(output_path)
    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    newImg.save(output_path)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python genmoji.py <user_prompt>")
        sys.exit(1)

    user_prompt = sys.argv[1]
    main(user_prompt)
