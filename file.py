# Teacher: Jerrad Flores
# Student: Thomas Wang
# School: Coding Minds Academy; 2021

# file.py
# Deals with file-management for the program.

import os

def image_files():
  # Returns a list of file names with the extension ".jpg"
  images = []
  for f in os.listdir():
    if f.endswith(".jpg"):
      images.append(f)
  return images