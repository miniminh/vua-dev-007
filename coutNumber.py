#Just for count the number of images 
import os

def count_items_in_folder(folder_path):
    if not os.path.isdir(folder_path):
        return f"{folder_path} is not a valid directory."
    items = os.listdir(folder_path)
    num_items = len(items)
    print(f"There are {num_items} items in the folder {folder_path}.")
    return num_items

folder_path = 'downloaded_images'
count_items_in_folder(folder_path)
