from mflux import Flux1, Config, ModelConfig
import os


def generate_image(prompt: str):
    # Load the model
    flux = Flux1(
        model_config=ModelConfig.FLUX1_DEV,
        quantize=8,
        lora_paths=[
            f"{os.path.abspath(os.path.dirname(__file__))}/lora/flux-dev.safetensors"
        ],
        lora_scales=[1.0],
    )

    # Generate an image
    image = flux.generate_image(
        seed=7,
        prompt=prompt,
        config=Config(
            num_inference_steps=20,
            height=160,
            width=160,
        ),
    )

    return image.image
