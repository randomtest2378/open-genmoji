from huggingface_hub import hf_hub_download

REPO_ID = "EvanZhouDev/open-genmoji"
FILENAME = "flux-dev.safetensors"

print(
    "Downloaded weights to: "
    + hf_hub_download(repo_id=REPO_ID, filename=FILENAME, local_dir="./lora")
)
