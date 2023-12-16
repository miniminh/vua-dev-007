from transformers import SegformerImageProcessor, AutoModelForSemanticSegmentation
from PIL import Image
import requests
import matplotlib.pyplot as plt
import torch.nn as nn
import time
import numpy as np
import cv2

from utils import ID2LABEL

extractor = SegformerImageProcessor.from_pretrained("mattmdjaga/segformer_b0_clothes")
model = AutoModelForSemanticSegmentation.from_pretrained("mattmdjaga/segformer_b0_clothes")

def get_pred_seg(image):
    
    inputs = extractor(images=image, return_tensors="pt")
    outputs = model(**inputs)

    logits = outputs.logits.cpu()

    upsampled_logits = nn.functional.interpolate(
        logits,
        size=image.size[::-1],
        mode="bilinear",
        align_corners=False,
    )

    pred_seg = upsampled_logits.argmax(dim=1)[0]
    # print(pred_seg.tolist())
    return pred_seg

def process_pred_seg(image, pred_seg):
    
    masks = []
    crop_imgs = []
    clothing_types = []
    
    max_value = pred_seg.max()
    for value in range(0, max_value.item()):
        masks.append(pred_seg == value)

    for idx in range(0, max_value.item()):
        print(ID2LABEL[str(idx)])
        mask = np.array(masks[idx])
        mask = np.expand_dims(mask, axis=2)
        image_masked = np.where(mask, image, np.zeros_like(image))

        image_masked = np.array(image_masked)

        gray = cv2.cvtColor(image_masked, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)[1]
        contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = contours[0] if len(contours) == 2 else contours[1]
        try:
            cnt = max(contours, key=cv2.contourArea)
            x,y,w,h = cv2.boundingRect(cnt)

            extra = 20

            crop_img = image_masked[y - extra:y+h + extra, x - extra:x+w + extra]
            crop_img[np.where(crop_img==0)] = 255
            crop_imgs.append(crop_img)
            clothing_types.append(ID2LABEL[str(idx)])
        except:
            print("error")
    return crop_imgs, clothing_types



def get_segmentation(path):
    image = Image.open(path)
    pred_seg = get_pred_seg(image)
    crop_imgs, clothing_types = process_pred_seg(image, pred_seg)
    return crop_imgs, clothing_types
