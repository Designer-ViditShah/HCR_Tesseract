import pytesseract
import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import Dataset.IAM_Line_Dataset
import os
from PIL import Image
from preprocessing import preprocessing as pp


def preprocess(image):
    img = Image.open(image)
    return pp.preprocessing(img)


def get_string_from_pre_processed_image(pre_processed_image):
    recognized_string = "Demo check"
    return recognized_string


def print_both_lists(tesseract_string_values, cnn_generated_string):
    for i in range(len(tesseract_string_values)):
        a = tesseract_string_values[i]
        b = cnn_generated_string[i]
        print("Original Value : ", a, " \nPredicted Value: ", b)


if __name__ == '__main__':
    print("Convert Image To Text Started...")
    pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract"
    print("tesseract ocr execution starts")
    path = os.path.join(os.path.join(os.getcwd(),"Dataset"), "IAM_Line_Dataset")
    print(path)
    tesseract_string_values = []
    cnn_generated_string = []
    for image in os.listdir(path):
        if image.endswith(".png"):
            pre_processed_image = preprocess(os.path.join(path,image))
            tesseract_string_values.append(pytesseract.image_to_string(pre_processed_image))
            cnn_generated_string.append(get_string_from_pre_processed_image(pre_processed_image))
            print_both_lists(tesseract_string_values,cnn_generated_string)
            break
    print("Code terminated successfully.....")