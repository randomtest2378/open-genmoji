import sys
from promptAssistant import get_prompt_response
from generateImage import generate_image
from PIL import Image
import os
import argparse


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


def main(arguments, output_path: str = "output/genmoji.png"):
    user_prompt = arguments.user_prompt

    # if the user did not turn off prompt assist:
    if not arguments.direct:
        # Get the response from the prompt assistant
        prompt_response = get_prompt_response(user_prompt)
        print("\nPrompt Created: " + prompt_response)

    # if the user turned off prompt assist
    elif arguments.direct:
        prompt_response: str = arguments.user_prompt
        print("\nUsing original prompt: " + prompt_response)

    # Generate the image using the resulting prompt
    image = generate_image(prompt_response, arguments)

    width, height = image.size
    newImg = image.resize((width * arguments.upscale, height * arguments.upscale), Image.LANCZOS)

    output_path = get_unique_path(output_path)
    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    newImg.save(output_path)


if __name__ == "__main__":
    # When function is called it creates an object that looks like this:
    # Namespace(user_prompt='a squirrel holding an iphone', assist=True, lora='flux-dev', width=160, height=160, upscale=5)
    # the args object can then be passed into different functions

    # and its values can be accessed, for example, like this:
    # `args.height` --> returns `160` (as an int) by default

    parser = argparse.ArgumentParser()
    parser.add_argument("user_prompt", type=str, help="Your prompt")
    parser.add_argument("-d", "--direct",
                        action="store_true", help="Do not use prompt assistant")
    parser.add_argument("-l", "--lora",
                        nargs="?", default="flux-dev",
                        type=str, help="The LoRA to use")
    parser.add_argument("-iw", "--width",
                        nargs="?", default=160,
                        type=int, help="Image width")
    parser.add_argument("-ih", "--height",
                        nargs="?", default=160,
                        type=int, help="Image height")
    parser.add_argument("-u", "--upscale",
                        nargs="?", default=5,
                        type=int, help="Upscale factor")
    args = parser.parse_args()
    print(args)
    main(arguments=args)
