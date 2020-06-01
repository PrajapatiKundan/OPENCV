import numpy as np
from PIL import Image
import os, cv2

def train_classifier(data_dir):
    path = [ os.path.join(data_dir, file) for file in os.listdir(data_dir)]#[data/user.1.0.jpg....]
    faces = []
    ids = []

    for image_path in path:
        #image = data/user.1.0.jpg
        img = Image.open(image_path).convert('L')#cvt in gray image
        image_np = np.array(img, 'uint8')
        #os.path.split(/home/User/Desktop/file.txt) return (/home/User/Desktop/, file.txt)=>tuple
        f_name = os.path.split(image_path)[1]
        id = int(f_name.split(".")[1])#("user", "1", "0")

        faces.append(image_np)
        ids.append(id)

    ids = np.array(ids)
    clf = cv2.face.LBPHFaceRecognizer_create()
    clf.train(faces, ids)
    clf.write("classifier.yml")

train_classifier("data")