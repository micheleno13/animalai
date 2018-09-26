from PIL import Image
import os, glob
import numpy as np
from sklearn import model_selection

SAVE_DATA_DIR = os.path.join("image_data")
ANIMAL_TYPES = ["monkey", "boar", "crow"]
NUM_ANIMAL_TYPE = len(ANIMAL_TYPES)
IMAGE_SIZE = 50

X = []
y = []

for index, animal_type in enumerate(ANIMAL_TYPES):
    image_files = glob.glob(os.path.join(SAVE_DATA_DIR, animal_type, "*.jpg"))

    for i, image_file in enumerate(image_files):
        if i >= 200:
            break;

        image = Image.open(image_file)
        image = image.convert("RGB")
        image = image.resize((IMAGE_SIZE, IMAGE_SIZE))
        data = np.asarray(image)
        X.append(data)
        y.append(index)

X = np.array(X)
y = np.array(y)

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y)
Xy = (X_train, X_test, y_train, y_test)

np.save("./animal.npy", Xy)
