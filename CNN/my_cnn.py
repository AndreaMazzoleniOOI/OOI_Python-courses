import glob
import cv2 as cv
import random
import matplotlib.pyplot as plt
from src.create_dataset import Dataset
from src.model import ModelParams
import tensorflow as tf
print(tf.test.is_gpu_available())
print(tf.test.is_built_with_cuda())

from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras import backend
backend.set_image_data_format('channels_first')
import os


def main():
    # Load model params, dataset, create labels
    params = ModelParams(file_path='config/system_configuration.json')
    paths_dir = [f'img/{p}' for p in os.listdir('img')]
    data = Dataset(dir_paths=paths_dir, size=50)
    data.info()

    # Create CNN struct
    model = Sequential()
    model.add(Convolution2D(params.nb_filters, params.nb_conv, padding='same', input_shape=data.x_train.shape[1:]))
    model.add(Activation('relu'))
    model.add(Convolution2D(params.nb_filters, params.nb_conv))
    model.add(MaxPooling2D(pool_size=(params.nb_pool, params.nb_pool)))
    model.add(Dropout(0.5))
    model.add(Flatten())
    model.add(Dense(params.nb_dense))
    model.add(Dropout(0.5))
    model.add(Dense(params.nb_classes))
    model.add(Activation('sigmoid'))
    model.compile(loss='sparse_categorical_crossentropy', optimizer='adadelta', metrics=['accuracy'])
    model.summary()
    # Train
    epochs = 1
    batch = 5
    model.fit(data.x_train, data.y_train, batch_size=batch, epochs=epochs, validation_data=(data.x_test, data.y_test))

if __name__=='__main__':
    main()