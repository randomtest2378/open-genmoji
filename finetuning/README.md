# Training Open Genmoji

Here's how you can train Open Genmoji yourself, either with a different set of emojis, train Open Genmoji with more training steps, use a different model, or just for fun!

See the README in the `lora` folder for more information about what models have already been trained.

**This guide offers a way to **

## Getting Started

First, you'll need to get the Emojis that you want to train on. In the end, you want a single directory with pairs of images and text descriptions of the image

```
trainingData/
├─ img1.txt
├─ img1.png
├─ img2.txt
├─ img2.png
├─ img3.txt
├─ img3.png

... and so on
```