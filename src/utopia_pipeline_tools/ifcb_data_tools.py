""" IFCB Data Tools Module

Contains funcitons to work with locally hosted IFCB images before CNN-
classification. 

(Probably adapted from functions in ifcb tools repo (add link))

- retrieve_filepaths_from_local(folder_location): Creates a list of IFCB .png
  filepaths from a local 'ml' folder. 
"""

# imports
import os
import re

def retrieve_filepaths_from_local(folder_location):
    """ Retrieves filepaths of all IFCB images in the specified processed data 
    folder location (local). Returns a list of all image filepaths in the ml 
    sub-folders.

    :param folder_location: Filepath to the ml folder location
    :type folder_location: str
    """
    # list all folders in the ml folder
    sub_folders = os.listdir(folder_location)
    image_list = []

    # loop over sub-folder locations to retrieve all images
    for folder in sub_folders:
        sub_folder_loc = os.path.join(folder_location, folder)

        if not os.path.isdir(sub_folder_loc):
            continue

        images = os.listdir(sub_folder_loc)

        for image in images:
            im_filepath = os.path.join(sub_folder_loc, image)
            image_list.append(im_filepath)

    return image_list