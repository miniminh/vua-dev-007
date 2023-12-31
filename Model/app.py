from fastapi import FastAPI, UploadFile, HTTPException, BackgroundTasks, File, Query
from typing import Union
from typing_extensions import Annotated
from fastapi.responses import FileResponse, RedirectResponse
from uvicorn import run
import shutil
import os
import numpy as np
import cv2
import pickle 
from joblib import dump, load
from merger import merge

from segmentation import get_segmentation
from clustering import get_embedding, transform_new_image, get_file_list, save_and_extract, create_new_embedding
from utils import plot_embedding

DO_MERGE = True
ALLOWED_IMAGE_TYPES = ["image/jpeg", "image/png", "image/bmp"]

print(f"Getting embedding")
brand = 'adidas'
# path = f'{brand}_images'
# embedding, file_list = get_embedding(path)

# with open(f'{brand}_embedding.pkl', 'wb') as f:
#     pickle.dump(embedding, f)

# with open(f'{brand}_file_list.pkl', 'wb') as f:
#     pickle.dump(file_list, f)


with open(f'{brand}_embedding.pkl', 'rb') as f:
    embedding = pickle.load(f)

with open(f'{brand}_file_list.pkl', 'rb') as f:
    file_list = pickle.load(f)

print("Get embedding complete!")


def save_upload_file(upload_file, destination):
    try:
        with destination.open("wb") as buffer:
            shutil.copyfileobj(upload_file.file, buffer)
    finally:
        upload_file.file.close()


app = FastAPI()

@app.get("/")
async def test_get():
    return "hello! lai la Minh day!"

@app.post("/api/upload/")
async def upload_file(
    input: UploadFile = File(...)
    
): 
    print("Received request?")
     
    filename = input.filename
    await input.seek(0)
    
    # try:
    filename.replace(" ", "")
    print(filename)
    path = f"uploads/{filename}"
    with open(path, "wb+") as file_object:
        shutil.copyfileobj(input.file, file_object)   
    # except:
    #     raise HTTPException(status_code=403, detail="Upload file is corrupted") 
    # finally:    
    input.file.close()
    
    crop_imgs, clothing_types = get_segmentation(path)
    
    
    if DO_MERGE:
        features = []
        null_features = []
        for crop_img, clothing_type in zip(crop_imgs, clothing_types):
            if clothing_type not in ['Upper-clothes', 'Pants']:
                null_features.append(None)
                continue
            _, feature = save_and_extract(crop_img)
            features.append(feature.squeeze())
            null_features.append(feature.squeeze())
            
        features = np.array(features)
        style_vector = merge(features) 
        nearest = {}
        for crop_img, clothing_type, feature in zip(crop_imgs, clothing_types, null_features):
            if clothing_type not in ['Upper-clothes', 'Pants']:
                continue
            nearest[clothing_type] = []
            concat_vector = np.concatenate([style_vector, feature.reshape(1,-1)])
            merge_feature = merge(concat_vector)
            new_embedding = create_new_embedding(merge_feature, embedding)
            if new_embedding is not None:
                # plot_embedding(crop_img, embedding, file_list, new_embedding, new_file_list)
                nearest_id = np.argpartition((np.linalg.norm(embedding - new_embedding, axis=1)), 2)[:2]
                for id in nearest_id:
                    nearest[clothing_type].append(file_list[id])
    else:
        nearest = {}
        
        for crop_img, clothing_type in zip(crop_imgs, clothing_types):
            nearest[clothing_type] = []
            new_embedding, new_file_list = transform_new_image(crop_img, embedding)
            if new_embedding is not None:
                # plot_embedding(crop_img, embedding, file_list, new_embedding, new_file_list)
                nearest_id = np.argpartition((np.linalg.norm(embedding - new_embedding, axis=1)), 2)[:2]
                for id in nearest_id:
                    nearest[clothing_type].append(file_list[id])
                    
    print(nearest)
    return nearest

if __name__ == "__main__":
    
    run('app:app', 
        host="0.0.0.0", 
        port=14024, 
        reload=True
        )