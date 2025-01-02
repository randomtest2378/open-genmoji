import sys
from promptAssistant import get_prompt_response
from generateImage import generate_image
from PIL import Image
import os
import json


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


def main(
    user_prompt: str,
    output_path: str = "output/genmoji.png",
    lora: str = "flux-dev",
):
    with open("./lora/info.json", "r") as f:
        models = json.load(f)
        metaprompt = "open-genmoji"
        found = False
        for model in models:
            if model["name"] == lora:
                found = True
                metaprompt = model["metaprompt"]
                break

        if not found:
            print(
                f"Error: LoRA {lora} does not exist. Run 'python download.py' to view and download available LoRAs."
            )
            sys.exit(1)

        # Check if the lora file exists
        lora_path = f"lora/{lora}.safetensors"
        if not os.path.exists(lora_path):
            print(
                f"Error: LoRA {lora} is not downloaded. Please run 'python download.py' to download it."
            )
            sys.exit(1)

        # Get the response from the prompt assistant
        prompt_response = get_prompt_response(user_prompt, metaprompt)
        print("Prompt Created: " + prompt_response)

        # Generate the image using the response from the prompt assistant
        image = generate_image(prompt_response, lora)

        width, height = image.size
        newImg = image.resize((width * 5, height * 5), Image.LANCZOS)

        output_path = get_unique_path(output_path)
        # Create output directory if it doesn't exist
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        newImg.save(output_path)


if __name__ == "__main__":
    if len(sys.argv) not in [2, 3]:
        print("Usage: python genmoji.py [<lora>] <user_prompt>")
        sys.exit(1)

    if len(sys.argv) == 3:
        lora = sys.argv[1]
        user_prompt = sys.argv[2]
    else:
        lora = "flux-dev"
        user_prompt = sys.argv[1]

    main(user_prompt, lora=lora)
