![](./assets/openGenmoji.png)

## What is Open Genmoji?

Open Genmoji attempts to recreate Apple's Genmoji feature, but with open technology! You can run Open Genmoji models anywhere (on device, server, etc.) and more importantly, on any system... it's no longer restricted to just Apple devices!

At its core, Open Genmoji is simply a small LoRA file that tells a Image Generation model how to create emojis. So, anywhere you can add a LoRA onto an image generation model, you can use Open Genmoji.

There's built in scripts here to help you generate optimal prompts for your image models to create the best emoji, and also scripts to help you finetune your very own Open Genmoji model.

See info about finetuning Open Genmoji yourself in the `finetuning` folder.

## Running Open Genmoji on Mac

> **Note**: This guide is optimized for running Flux with LoRA on Mac. If you are using other systems, feel free to search for a guide online for using LoRA with Flux (there are many!)... **I still recommend reading through this, since it also includes info on the Open Genmoji Prompt Assist, which may be helpful**

All available LoRAs are in the `lora` folder. Refer to the `README` in that folder to see which ones are for which models. In this quick guide, I'll go over how to run the LoRA with `mflux` (for Apple Silicon) and then how to use the Open Genmoji Prompt Assistant to generate enhanced prompts.

### Using `mflux`

First, clone Open Genmoji:

```
git clone https://github.com/EvanZhouDev/open-genmoji.git
```

Next, create a `venv` here with your method of choice. If you use `mise`, there's already a `mise.toml`. The recommended version of Python is 3.11. Some things may not work with other versions.

Now, you can just run the following `mflux` command:

```bash
mflux-generate --model dev --prompt "your prompt" --steps 10 --seed 2 -q 8 --width 160 --height 160 --lora-paths "./lora/flux-dev.safetensors" --guidance 5.0
```

These are the recommended settings.

## Prompt Assist

Prompt Assist is an additional LLM layer on top of Open Genmoji which helps you create the perfect prompt for generating emojis. The metaprompt for Prompt Assist is in `PROMPT.md`. You can choose to run it anywhere you want, like ChatGPT; just attach `USER PROMPT: [emoji description]` at the end to trigger the prompt to give you a description. The result should be something like when you provide it with "flying pig":

```
emoji of flying pink pig. enlarged head in cartoon style. cute. white wings. head is turned towards viewer. 3D lighting. no cast shadows.
```

## Running Prompt Assist with `mflux`

This is more or less my own setup to locally run Prompt Assist and directly feed it into `mflux`, but I decided to push it in case anyone else wants to use it too.

First, you will need to install [LM Studio](https://lmstudio.ai/). Download your favorite local model.

Now, while that's downloading, create a `venv` in this directory and install these dependencies:

```
pip install mflux pillow requests
```

Now, when everything's done, spin up the development server on LM Studio.

Then, you can simply run:

```
python3 genmoji.py "[your prompt]"
```

And it'll first generate a prompt with LM Studio, and feed that into `mflux`.
