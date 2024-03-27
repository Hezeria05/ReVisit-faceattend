import cv2
import numpy as np
import os

#algorithm integration in face recognition

def load_face_data(dirpath):
    face_data = []
    labels = []
    name = {}
    class_id = 0

    for file in os.listdir(dirpath):
        if file.endswith(".npy"):
            data_item = np.load(os.path.join(dirpath, file))
            name[class_id] = file[:-4]
            face_data.append(data_item)
            target = class_id * np.ones((data_item.shape[0],))
            class_id += 1
            labels.append(target)

    face_dataset = np.concatenate(face_data, axis=0)
    face_dataset = np.array([i.flatten() for i in face_dataset])
    face_labels = np.concatenate(labels)

    return face_dataset, face_labels, name

def distance(x, X):
    return np.sqrt(np.sum((x-X)**2))

def KNN(X, Y, x, K=5):
    m = X.shape[0]
    x = x.flatten()
    val = []
    for i in range(m):
        xi = X[i]
        dist = distance(x, xi)
        val.append((dist, Y[i]))
    val = sorted(val, key=lambda x: x[0])[:K]
    val = np.array(val)
    labels = val[:, 1]
    unique_labels, counts = np.unique(labels, return_counts=True)
    index = counts.argmax()
    prediction = unique_labels[index]
    return prediction
