import os
import numpy as np
import cv2 as cv
import glob
import json


class ModelParams:
    def __init__(self, file_path='./config/system_configuration.json'):
        """
        :param file_path: *.json file path with configuration data.

        Load json file with CCN model parameters
        You can develop your own custom object by adding the wanted field to the json file and add them to the
        self.__read_file() and self.__write_file() methods.
        """

        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"{file_path} cannot be found")

        self.config = {}
        self.file_path = file_path
        self.__read_config()

    def __read_config(self):
        """Read file from file and update self.config"""

        with open(self.file_path, 'r', encoding='utf-8') as f:
            file = json.load(f)
        f.close()
        # ADD CUSTOM FIELDS IN CONFIG IF NEEDED
        config = {
            'batch_size': file['Batch Size'],
            'nb_classes': file['Class Number'],
            'nb_epochs': file['Epochs'],
            'nb_filters': file['Filters'],
            'nb_pool': file['Max Pooling'],
            'nb_conv': file['Convolutional Layers'],
            'nb_dense': file['Dense Layers']
        }
        self.config = config

    @property
    def batch_size(self):
        return self.config['batch_size']

    @property
    def nb_classes(self):
        return self.config['nb_classes']

    @property
    def nb_epoch(self):
        return self.config['nb_epoch']

    @property
    def nb_filters(self):
        return self.config['nb_filters']

    @property
    def nb_pool(self):
        return self.config['nb_pool']

    @property
    def nb_conv(self):
        return self.config['nb_conv']

    @property
    def nb_dense(self):
        return self.config['nb_dense']
