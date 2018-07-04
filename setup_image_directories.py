import os
import pandas as pd
import shutil

# arrange images in directories by class labels

current_dir = os.getcwd()
print(current_dir)
default_image_dir = os.path.join(current_dir, "data/train")
default_csv_path = os.path.join(current_dir, "data/train.csv")
print(default_csv_path)


def create_directories_from_labels(labels, working_dir=None):
    if working_dir is None:
        working_dir = default_image_dir
    for label in labels:
        #print(label)
        dir_path = os.path.join(working_dir, label)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)


def move_images(image_names, labels, source_image_dir=None, dest_image_dir=None):
    if len(image_names) != len(labels):
        print("Error: images and labels don't align")
        return
    if source_image_dir is None:
        source_image_dir = default_image_dir
    if dest_image_dir is None:
        dest_image_dir = source_image_dir
    for i, image in enumerate(image_names):
        source_image_path = os.path.join(source_image_dir, image)
        dest_image_path = os.path.join(dest_image_dir, labels[i], image)
        if os.path.isfile(source_image_path):
            shutil.move(src=source_image_path, dst=dest_image_path)


def setup_image_directories(image_dir=None, csv_path=None):
    if image_dir is None:
        image_dir = default_image_dir
    if csv_path is None:
        csv_path = default_csv_path
    print(csv_path)
    df = pd.read_csv(csv_path)
    labels = list(df.Id)
    image_names = list(df.Image)
    create_directories_from_labels(labels, image_dir)
    move_images(image_names, labels, image_dir, image_dir)

setup_image_directories()
