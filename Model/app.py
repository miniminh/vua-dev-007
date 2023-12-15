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

from segmentation import get_segmentation
from clustering import get_embedding, transform_new_image, get_file_list
from utils import plot_embedding

ALLOWED_IMAGE_TYPES = ["image/jpeg", "image/png", "image/bmp"]

def save_upload_file(upload_file, destination):
    try:
        with destination.open("wb") as buffer:
            shutil.copyfileobj(upload_file.file, buffer)
    finally:
        upload_file.file.close()


path = 'downloaded_images'
print(f"Getting embedding from {path}")
# embedding, file_list = get_embedding(path)
print("Get embedding complete!")

# dump(embedding, 'embedding.joblib') 
embedding = load('embedding.joblib') 
# with open('embedding.pkl', 'wb') as f:
#     pickle.dump(embedding, f)

# with open('file_list.pkl', 'wb') as f:
#     pickle.dump(file_list, f)

with open('file_list.pkl', 'rb') as f:
    file_list = pickle.load(f)

# print(file_list)
# embedding = np.load('embedding.npy')


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
    crop_imgs = get_segmentation(path)
    new_embedding, new_file_list = transform_new_image(crop_imgs, embedding)
    plot_embedding(crop_imgs, embedding, file_list, new_embedding, new_file_list)
    nearest_id = np.argpartition((np.linalg.norm(embedding - new_embedding, axis=1)), 2)
    # print(file_list[nearest_id[0]])
    return nearest_id

if __name__ == "__main__":
    run('app:app', 
        host="0.0.0.0", 
        port=14024, 
        reload=True
        )