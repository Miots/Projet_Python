import tensorflow as tf
import numpy as np
import cv2

model = tf.keras.applications.MobileNetV2(weights='imagenet')

image = cv2.imread('image.webp')