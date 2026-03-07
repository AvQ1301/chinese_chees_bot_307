from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import os

label_path = datasets/train/labels/0a426c3e-Untitled-146_jpg.rf.231702240f0fbebc95babead99defc0b.txt
img_path = label_path.replace(labels, images).rsplit('.', 1)[0] + .jpg

if not os.path.exists(label_path):
    raise FileNotFoundError(label_path)
if not os.path.exists(img_path):
    raise FileNotFoundError(img_path)

with open(label_path, 'r') as f:
    line = f.readline().strip()
if not line:
    raise ValueError('Label file is empty')
parts = line.split()
if len(parts) < 5:
    raise ValueError('Label line malformed: ' + line)
cls = parts[0]
cx, cy, w, h = map(float, parts[1:5])

img = Image.open(img_path).convert('RGB')
W, H = img.size
# YOLO center format -> pixel coords
left = (cx - w / 2) * W
top = (cy - h / 2) * H
right = (cx + w / 2) * W
bottom = (cy + h / 2) * H

draw = ImageDraw.Draw(img)
draw.rectangle([left, top, right, bottom], outline='red', width=4)

plt.figure(figsize=(8, 8))
plt.imshow(img)
plt.axis('off')
plt.show()

out = 'datasets/train/images/0a426c3e_bbox_preview.jpg'
img.save(out)
print('Saved preview to', out)
