import os
import shutil
import random

crop_path = r"C:\Users\DELL\Desktop\new_work\crop"
no_crop_path = r"C:\Users\DELL\Desktop\new_work\no_crop"

base_path = r"C:\Users\DELL\Desktop\dataset"

train_path = os.path.join(base_path, "train")
val_path = os.path.join(base_path, "val")

classes = {
    "crop": crop_path,
    "no_crop": no_crop_path
}

for cls, path in classes.items():
    images = [img for img in os.listdir(path) if img.endswith(('.jpg', '.png', '.jpeg'))]
    random.shuffle(images)

    split = int(0.8 * len(images))
    train_imgs = images[:split]
    val_imgs = images[split:]

    os.makedirs(os.path.join(train_path, cls), exist_ok=True)
    os.makedirs(os.path.join(val_path, cls), exist_ok=True)

    for img in train_imgs:
        shutil.copy(os.path.join(path, img),
                    os.path.join(train_path, cls, img))

    for img in val_imgs:
        shutil.copy(os.path.join(path, img),
                    os.path.join(val_path, cls, img))

print("Done splitting dataset.")