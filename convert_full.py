import os
from PIL import Image

INPUT_DIR = "assets/img/full/ourlovelyguests/momentofjoy"
OUTPUT_DIR = "assets/img_download/ourlovelyguests/momentofjoy"

QUALITY = 92  # rất cao

for root, _, files in os.walk(INPUT_DIR):
    for file in files:
        if file.lower().endswith((".jpg", ".jpeg", ".png")):
            input_path = os.path.join(root, file)
            rel = os.path.relpath(input_path, INPUT_DIR)
            out = os.path.join(
                OUTPUT_DIR,
                os.path.splitext(rel)[0] + ".webp"
            )

            img = Image.open(input_path).convert("RGB")
            os.makedirs(os.path.dirname(out), exist_ok=True)
            img.save(out, "WEBP", quality=QUALITY, method=6)

            print(f"✔ {rel}")
