import os
import re


dir_list = []
root_directory = r'C:\Users\Reta\Downloads\JavaScript Free Tutorial for beginners in Hindi Urdu'


def get_all_subdirs():
    for root, dirs, files in os.walk(root_directory):
        path = os.path.abspath(root)
        dir_list.append(path)
    return dir_list
