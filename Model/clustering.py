import tensorflow as tf
import numpy as np
import cv2
from tqdm import tqdm
import glob
from openTSNE import TSNE
import matplotlib.pyplot as plt
from multiprocessing import Pool

from utils import get_temp_name

model = tf.keras.applications.MobileNetV3Small(
    input_shape=(100, 100, 3),
    include_top=False
)

def get_file_list(path):
    file_list = [] 
    for filepath in glob.iglob(f'{path}/*.*'):
        file_list.append(filepath)
    return file_list

def process_file_list(file_list):
    images = []
    for filename in tqdm(file_list):
        img = cv2.imread(filename)
        img = cv2.resize(img, (100, 100))
        images.append(img)
    return images

def feature_extraction(img, squeeze=True):
    img = np.expand_dims(img, axis=0)
    feature = model(img)
    flat_feature = np.array(feature).reshape(1, -1)
    if squeeze:
        flat_feature = flat_feature.squeeze()
    return flat_feature

def get_embedding(images_path='downloaded_images'):
    file_list = get_file_list(images_path)
    images = process_file_list(file_list)
    with Pool(5) as p:
        img_features = list(p.map(feature_extraction, tqdm(images)))
    tsne = TSNE(
        n_components=2,
        perplexity=30,
        metric="euclidean",
        random_state=42,
        verbose=True,
    )
    embedding = tsne.fit(np.array(img_features))
    return embedding, file_list

def save_and_extract(crop_img):
    temp_filename = get_temp_name()
    temp_filename = "cache/" + temp_filename + ".jpg"
    plt.imsave(temp_filename, crop_img)
    
    crop_img = cv2.resize(crop_img, (100, 100))
    new_image = feature_extraction(crop_img, squeeze=False)
    new_image = np.array(new_image)
    return temp_filename, new_image

def create_new_embedding(new_image, embedding):
    print(embedding.shape, new_image.shape)
    new_embedding = embedding.transform(np.array(new_image))
    return new_embedding

def transform_new_image(crop_img, embedding):
    try: 
        temp_filename, new_image = save_and_extract(crop_img)
        
        new_file_list = []
        new_file_list.append(temp_filename)
        
        new_embedding = create_new_embedding(new_image, embedding)
        
        return new_embedding, new_file_list
    except: 
        print("error with file?")
        return None, None