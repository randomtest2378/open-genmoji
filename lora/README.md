# Open Genmoji LoRAs

## Downloading LoRAs

Downloads are done through HuggingFace. Run the following Python script in the root `open-genmoji` directory to download the file here:

```bash
# If you're in the lora directory, cd out to root `open-genmoji` folder
cd ../

python3 ./download.py
```

## LoRA List

List of metadata for all Genmoji LoRAs.

| LoRA Name              | Model Trained | Emojis Used                   | More Info                    |
| ---------------------- | ------------- | ----------------------------- | ---------------------------- |
| `flux-dev.safetensors` | Flux.1 Dev    | No Skintone Emoji List (1901) | [View](#flux-devsafetensors) |
| [`diverse-emoji.safetensors`](https://huggingface.co/caspersimon/Diverse-Emoji/) | Flux.1 Dev    | Complete Apple Emoji list (3770) | [View](#diverse-emojisafetensors) |

# Contributing a LoRA

Feel free to create your own LoRAs, and they can be added here if you want! Reference the `LORA_TEMPLATE.md` file in this directory for adding the description below. You can submit as a PR here with Git LFS, and I will sync it to HuggingFace.

# Detailed LoRA Description

## `flux-dev.safetensors`

**Model Finetuned**: Flux.1 Dev
**Finished Finetuning**: December 25, 2024
**Finetuned By**: Evan Zhou ([@evanzhoudev](https://github.com/evanzhoudev))
**Finetuned On**: M4 Max MacBook Pro (64GB Unified Memory)
**Finetuned With**: [SimpleTuner](https://github.com/bghira/SimpleTuner)
**Finetuning Time**: ~10 hours
**Finetuning Steps**: 10,000
**Image Resolution**: 160x160
**Emoji Dataset**: All Apple Emojis as of December 25, 2024, with skin tone variants pruned to reduce training time.

## `diverse-emoji.safetensors`

**Model Finetuned**: Flux.1 Dev
**Finished Finetuning**: December 31, 2024
**Finetuned By**: Julius ([@caspersimon](https://github.com/caspersimon))
**Finetuned On**: M4 Max MacBook Pro (128GB Unified Memory, 40 core GPU)
**Finetuned With**: [SimpleTuner](https://github.com/bghira/SimpleTuner)
**Finetuning Time**: ~20 hours
**Finetuning Steps**: 20,000
**Image Resolution**: 160x160
**Emoji Dataset**: All Apple Emoji as of December 30, 2024.
[**Huggingface link**](https://huggingface.co/caspersimon/Diverse-Emoji)
