import os
from PIL import Image

INPUT_DIR = "assets/img/full/bridgegroom"
OUTPUT_DIR = "assets/img_webp/bridgegroom"

MAX_WIDTH = 2000      # resize nếu ảnh quá lớn
QUALITY = 80          # 75–85 là đẹp cho web

def convert_image(input_path, output_path):
    img = Image.open(input_path).convert("RGB")

    # resize nếu quá lớn
    if img.width > MAX_WIDTH:
        ratio = MAX_WIDTH / img.width
        new_size = (MAX_WIDTH, int(img.height * ratio))
        img = img.resize(new_size, Image.LANCZOS)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path, "WEBP", quality=QUALITY, method=6)

def run():
    for root, _, files in os.walk(INPUT_DIR):
        for file in files:
            if file.lower().endswith((".jpg", ".jpeg", ".png")):
                input_path = os.path.join(root, file)

                rel_path = os.path.relpath(input_path, INPUT_DIR)
                output_path = os.path.join(
                    OUTPUT_DIR,
                    os.path.splitext(rel_path)[0] + ".webp"
                )

                convert_image(input_path, output_path)
                print(f"✔ {rel_path}")

    print("\n🎉 Convert xong toàn bộ ảnh!")

if __name__ == "__main__":
    run()
