import glob
import cv2 as cv
import random
import numpy as np


class Dataset:
    def __init__(self, dir_paths: list, size=1000, split=0.7, image_extension='jpg'):
        self.dir_paths = dir_paths
        self.size = size
        self.image_extension = image_extension
        self.__x, self.__y = self.create_labels_from_paths()
        self.__n_images = len(self.__x)
        self.__x_train = self.__x[:int(split * self.__n_images)]
        self.__x_test = self.__x[int(split * self.__n_images):]
        self.__y_train = self.__y[:int(split * self.__n_images)]
        self.__y_test = self.__y[int(split * self.__n_images):]

    def create_labels_from_paths(self):
        x, y = [], []
        for i, path_dir in enumerate(self.dir_paths):
            paths = glob.glob(f'{path_dir}/*.{self.image_extension}')
            for path in paths:
                img = cv.imread(path)
                img = cv.resize(img, (self.size, self.size))
                img = np.transpose(img, (2, 0, 1))
                img = np.reshape(img, (3, self.size, self.size))
                x.append(img/255)
                y.append(i)
        return np.array(x), np.array(y)

    def info(self):
        print(f'Dataset: {self.__n_images}')
        print(f'Size of x_train: {self.__x_train.shape}')
        print(f'Size of y_train: {self.__y_train.shape}')
        print(f'Size of x_test: {self.__x_test.shape}')
        print(f'Size of y_test: {self.__y_test.shape}')
        return

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def n_images(self):
        return self.__n_images

    @property
    def x_test(self):
        return self.__x_test

    @property
    def x_train(self):
        return self.__x_train
    @property
    def y_test(self):
        return self.__y_test

    @property
    def y_train(self):
        return self.__y_train
