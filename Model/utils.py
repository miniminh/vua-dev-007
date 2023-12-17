from time import gmtime, strftime
import string
import random
import matplotlib.pyplot as plt
import cv2
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
  return ''.join(random.choice(chars) for _ in range(size))

ID2LABEL = {
    "0": "Background",
    "1": "Hat",
    "2": "Hair",
    "3": "Sunglasses",
    "4": "Upper-clothes",
    "5": "Skirt",
    "6": "Pants",
    "7": "Dress",
    "8": "Belt",
    "9": "Left-shoe",
    "10": "Right-shoe",
    "11": "Face",
    "12": "Left-leg",
    "13": "Right-leg",
    "14": "Left-arm",
    "15": "Right-arm",
    "16": "Bag",
    "17": "Scarf"
  }

def get_temp_name():
  random_string = id_generator()
  date = strftime("%H_%M_%S_%d_%m_%Y", gmtime())
  return date + random_string

def get_image(path, zoom=0.3):
    try:
      image = plt.imread(path)
    except:
      image = plt.imread(path, -1)
    image = cv2.resize(image, (100, 100))
    return OffsetImage(image, zoom=zoom)
  
def plot_embedding(crop_imgs, embedding, file_list, new_embedding = None, new_file_list = None):
  fig, ax = plt.subplots()
  fig.set_figheight(50)
  fig.set_figwidth(50)
  ax.scatter(embedding.T[0], embedding.T[1])

  for i in range(len(crop_imgs)):
    ab = AnnotationBbox(get_image(file_list[i]), (embedding[i, 0], embedding[i, 1]), frameon=False)
    ax.add_artist(ab)
  for i in range(len(new_file_list)):
    ab = AnnotationBbox(get_image(new_file_list[i], zoom=1), (new_embedding[i, 0], new_embedding[i, 1]), frameon=False)
    ax.add_artist(ab)
  
  fig.savefig('embedding.png')