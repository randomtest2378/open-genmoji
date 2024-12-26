# Open Genmoji LoRAs

List of metadata for all Genmoji LoRAs.

| LoRA Name              | Model Trained | Emojis Used                   | More Info                    |
| ---------------------- | ------------- | ----------------------------- | ---------------------------- |
| `flux-dev.safetensors` | Flux.1 Dev    | No Skintone Emoji List (1901) | [View](#flux-devsafetensors) |

# Contributing a LoRA

Feel free to create your own LoRAs, and add it here! Reference the `LORA_TEMPLATE.md` file in this directory for adding the description below.

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
