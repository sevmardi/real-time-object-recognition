import coremltools
import keras
import tensorflow
from keras.models import load_model
from keras.utils.generic_utils import CustomObjectScope
import os
import sys
import glob
import argparse
import numpy as np
from PIL import Image
from scipy.misc import toimage
from matplotlib import pyplot as plt
from keras.datasets import cifar10
from keras.applications.mobilenet import MobileNet, preprocess_input
from keras.applications import mobilenet
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Model, load_model
from keras.layers import Dense, GlobalAveragePooling2D
from keras import backend as K
from keras.optimizers import SGD
from keras.utils import np_utils
from keras.layers import Input

# load model
model = load_model('keras/models/MobileNet_Oxford_IIIT.h5', custom_objects={
			   'relu6': mobilenet.relu6,
			   'DepthwiseConv2D': mobilenet.DepthwiseConv2D})
coreml_model = coremltools.converters.keras.convert(model)
