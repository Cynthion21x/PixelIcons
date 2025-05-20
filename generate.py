import os
from PIL import Image

# Fixed sizes to generate
sizes = [16, 24, 32, 48, 64, 96, 128, 256, 512]

# Source directory containing high-res icons
src_dir = 'apps/scalable'
dst_base = 'apps'

# Create destination folders if they don't exist
for size in sizes:
    os.makedirs(os.path.join(dst_base, str(size)), exist_ok=True)

# Process each PNG in the scalable folder
for filename in os.listdir(src_dir):
    if not filename.lower().endswith('.png'):
        continue

    src_path = os.path.join(src_dir, filename)
    with Image.open(src_path) as img:
        for size in sizes:
            resized = img.resize((size, size), resample=Image.NEAREST)
            dst_path = os.path.join(dst_base, str(size), filename)
            resized.save(dst_path)

print("Generated icons")

