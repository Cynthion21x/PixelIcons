import os
from PIL import Image

sizes = [16, 24, 32, 48, 64, 96, 128, 256, 512]

input = 'apps/icons'
output = 'apps'

# make folders
for size in sizes:
    os.makedirs(os.path.join(output, str(size)), exist_ok=True)

for filename in os.listdir(src_dir):

    if not filename.lower().endswith('.png'):
        continue

    inputF = os.path.join(input, filename)
    with Image.open(inputF) as img:
        for size in sizes:

            # scale using nearest neighbour so they are not blurry
            resized = img.resize((size, size), resample=Image.NEAREST)
            outputF = os.path.join(output, str(size), filename)
            resized.save(outputF)

print("Generated icons :D")

