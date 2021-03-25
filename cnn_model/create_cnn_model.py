import keras
import numpy as np
import matplotlib.pyplot as plt
from keras.preprocessing import image
from PIL import Image
import cv2
from keras.layers.convolutional import Convolution2D, MaxPooling2D, AveragePooling2D
from tensorflow.keras.layers import Conv1D
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import Conv3D
from tensorflow.keras.layers import Conv2DTranspose
from tensorflow.keras.layers import Conv3DTranspose
from tensorflow.keras.layers import SeparableConv1D
from tensorflow.keras.layers import SeparableConv2D
from tensorflow.keras.layers import DepthwiseConv2D
from tensorflow.keras.layers import UpSampling1D
from tensorflow.keras.layers import UpSampling2D
from tensorflow.keras.layers import UpSampling3D
from tensorflow.keras.layers import ZeroPadding1D
from tensorflow.keras.layers import ZeroPadding2D
from tensorflow.keras.layers import ZeroPadding3D
from tensorflow.keras.layers import Cropping1D
from tensorflow.keras.layers import Cropping2D
from tensorflow.keras.layers import Cropping3D

from keras.layers import Input, Dense, Dropout, Flatten, GlobalAveragePooling2D, Activation, BatchNormalization
from keras.models import Model, load_model
from keras.regularizers import l2
from keras.optimizers import SGD
from keras.initializers import RandomNormal
from keras.callbacks import ModelCheckpoint, LearningRateScheduler, ReduceLROnPlateau, CSVLogger

class create_cnn_model():
    model =
    return model;