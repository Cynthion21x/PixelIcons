import os
from PIL import Image

sizes = [32, 48, 64, 96, 128, 256, 512]
sizes_l = [16, 24]

input = 'apps/icons'
input_s = 'apps/icons-small'
output = 'apps'

for size in sizes:
    os.makedirs(os.path.join(output, str(size)), exist_ok=True)

for filename in os.listdir(input):

    if not filename.lower().endswith('.png'):
        continue

    inputF = os.path.join(input, filename)
    with Image.open(inputF) as img:

        print("resizing " + inputF)

        for size in sizes:

            resized = img.resize((size, size), resample=Image.NEAREST)
            outputF = os.path.join(output, str(size), filename)
            resized.save(outputF)

print("Generated large icons")

for size in sizes_l:
    os.makedirs(os.path.join(output, str(size)), exist_ok=True)

for filename in os.listdir(input_s):

    if not filename.lower().endswith('.png'):
        continue

    inputF = os.path.join(input_s, filename)
    with Image.open(inputF) as img:

        print("resizing " + inputF)

        for size in sizes_l:
            
            resized = img.resize((size, size), resample=Image.NEAREST)
            outputF = os.path.join(output, str(size), filename)
            resized.save(outputF)

print("Generated small icons")

print("finished :D")
