![](./assets/openGenmoji.png)

## What is Open Genmoji?

Open Genmoji attempts to recreate Apple's Genmoji feature, but with open technology! Open Genmoji works anywhere—Not just Apple devices.

At its core, Open Genmoji is simply a LoRA file, finetuned based on thousands of Apple emojis, that teaches an image generation model to create emojis. Anywhere you can add a LoRA onto an image generation model, you can use Open Genmoji.

Open Genmoji also comes with a built special metaprompt, known as [Open Genmoji Prompt Assist](#prompt-assist) to help you create the perfect prompt to make any emoji you want.

The best part? You can also [use your creation in iOS 18+ as a real emoji—Even](#postprocessing) if your phone doesn't support Apple Intelligence.

If you're experienced with Image Models, go to [Quickstart](#quickstart). Otherwise, check out the [Tutorial](#tutorial) for a full explanation.

## Table of Contents

- [Quickstart](#quickstart)
- [Prompt Assist](#prompt-assist)
- [Tutorial](#tutorial)
  - [Running Open Genmoji with `mflux`](#running-open-genmoji-with-mflux)
  - [Running Open Genmoji with Prompt Assist](#running-open-genmoji-with-prompt-assist)
  - [LM Studio Prompt Assist and `mflux` Workflow](#lm-studio-prompt-assist-and-mflux-workflow)
- [Postprocessing](#postprocessing)
- [Contributing](#contributing)

## Quickstart

> If you're looking for detailed steps to run the model, check out the [Tutorial](#tutorial)

If you know what you're doing, here's a quickstart guide:

- Get the LoRA for Flux.1 Dev in `lora/flux-dev.safetensors`
- A metaprompt for Open Genmoji is available in `METAPROMPT.md`, so you can create the perfect prompt. [Learn more here.](#prompt-assist)
- Run Flux.1 Dev with the LoRA. Check out [Postprocessing](#postprocessing) to learn how to use your creation as a real emoji in iOS 18

## Prompt Assist

Open Genmoji Prompt Assist is a metaprompt for Open Genmoji, to help you generate the perfect prompt for Open Genmoji finetuned models. Note that this metaprompt is specifically for Apple's emojis. If you are using/making a LoRA for Google, Microsoft, etc. emojis, this metaprompt will not work as well.

Here's an example of what Prompt Assist does:

| Input        | Output                                                                                                                                      |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `flying pig` | `emoji of flying pink pig. enlarged head in cartoon style. cute. white wings. head is turned towards viewer. 3D lighting. no cast shadows.` |

Now, you can focus on imagining the perfect emoji, while Prompt Assist helps you phrase it in a way that image models can understand.

The metaprompt is available in `METAPROMPT.md`. You can use this prompt in any LLM, such as ChatGPT, to generate a prompt for Open Genmoji.

Check out [LM Studio Prompt Assist and `mflux` Workflow](#lm-studio-prompt-assist-and-mflux-workflow) for my full workflow of using LM Studio and `mflux` together to run Open Genmoji on Mac.

## Tutorial

> This tutorial is specifically for Mac. However, Open Genmoji is completely adaptable for other operating systems. You will just need another tool to run Flux.1 Dev, with a LoRA.

If you're new to Image Generation or locally running models, this is the place for you. This guide will lead you through all the steps necessary to run Open Genmoji, and also use the Open Genmoji Prompt Assist metaprompt.

First, let's get started by simply running the model.

### Running Open Genmoji with `mflux`

The image model we'll be using in this guide is Flux.1 Dev. Open Genmoji takes the form of a LoRA, which is just a file that can teach the image model how to do something specific. In this case, create emojis!

First, **ensure you have [git-lfs](https://git-lfs.com/) installed**. You'll need it to pull the LoRA.

Then, clone this repository:

```bash
git clone https://github.com/EvanZhouDev/open-genmoji.git
```

The LoRA we'll be using is `lora/flux-dev.safetensors`.

Next, we'll need to install `mflux` on `pip`. This is a port of Flux, specifically for Mac. It's recommended we first create a `venv` and then install `mflux`:

```bash
# Create a venv, optional
python3 -m venv .venv
source .venv/bin/activate

# Install mflux
pip install -U mflux
```

Now, you're all good to go. Run the following command and you'll be able to create your first emoji. Play around with the prompt, and see what you can make. (If you're struggling with a good result, check out [Prompt Assist](#running-open-genmoji-with-prompt-assist))

```bash
mflux-generate \
    --model dev \
    --prompt "your prompt" \
    --steps 20 \
    --seed 2 \
    --quantize 8 \
    --guidance 5.0
    --width 160 \
    --height 160 \
    --lora-paths "./lora/flux-dev.safetensors"
```

### Running Open Genmoji with Prompt Assist

It's pretty difficult to get a good prompt to make a Apple-like emoji. Thus, we'll use a metaprompt... a prompt for an LLM, to make a prompt for Open Genmoji. Here's an example:

| Input        | Output                                                                                                                                      |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `flying pig` | `emoji of flying pink pig. enlarged head in cartoon style. cute. white wings. head is turned towards viewer. 3D lighting. no cast shadows.` |

The output prompt is now much better, and the generated emoji will be of much better quality.

You can run the metaprompt in any place an LLM is available, including ChatGPT! Go grab the prompt from `METAPROMPT.md`. Then, feed it to the LLM, and after it, include your user prompt. Something like this:

```
{METAPROMPT HERE}

USER PROMPT: {your input}
```

Then, take the LLM output and feed that to `mflux`. Observe how the output is much better!

Now that you have a image output, head on to [Postprocessing](#postprocessing) to start using your creation as an actual emoji on your iPhone, or learn a bit more below about how to chain Prompt Assist and `mflux` together.

### LM Studio Prompt Assist and `mflux` Workflow

It's a bit tedious to feed your own prompt to an LLM, then feed the LLM output to `mflux`. So I made a quick Python workflow to chain these things together.

It's a bit of a specific/personal setup, but I decided to push it in case anyone wants to use it too.

First, you will need to install [LM Studio](https://lmstudio.ai/). Download your favorite local model, and start the Development mode. It should be running on port `1234` (default).

Now, install these two dependencies (in addition to `mflux`):

```bash
pip install mflux pillow requests
```

Now, given that LM Studio is correctly set up, you should be able to directly run:

```bash
python3 genmoji.py "[your prompt]"
```

And it'll first generate a prompt with LM Studio, and feed that into `mflux`. The output should be saved by default in `output/genmoji-001.png` (Number will increase automatically).

> **Note**: Before it saves, it'll also do the Postprocessing step of resizing it to 5x the size with anti-aliasing (160x160 → 800x800). Learn more in [Postprocessing](#postprocessing)

Now, let's take a look at [Postprocessing](#postprocessing) to start using your creation as an actual emoji in iOS.

## Postprocessing

Now that you have a single output image, our first step is to resize to 800x800, with anti-aliasing, so that iOS's Sticker/Emoji system recognizes it. If you've used the all-in-one LM Studio/`mflux` workflow, this step is already done.

If you don't have it installed, first install `pillow` to do the following procedure:

```bash
pip install pillow
```

All you have to do is simply run `python3 resize.py path/to/your/image.png`. This should generate a new image conveniently with "resized" in the name.

Now, all you have to do is send this image over to your phone. Now, follow these simple steps to use it as a Sticker (iOS 17+) or Emoji (iOS 18+):

1. Open the image on your phone in Photos
2. Long press and hold on the emoji in your picture (**don't move your finger**), and release after ~2s
3. Press the **Add Sticker** button

Now, if you're on iOS 17+, you should be able to apply this sticker by dragging it onto a message.

If you're on iOS 18+, in your emoji menu, you can simply tap your sticker to use it inline just like an emoji.

If you want to delete the Sticker, long press and hold (**don't move your finger**) on the Sticker in the Sticker gallery and release after ~2s. Press **Delete**.

## Contributing

Open Genmoji is open to more LoRAs for:

- New models
- New/Different sets of emojis
- More training for existing emoji sets

Check out `finetuning/README.md` for more information about finetuning, and check out `lora/README.md` for the current available LoRAs.
