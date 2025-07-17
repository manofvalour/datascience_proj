import pandas as pd
from sklearn.linear_model import ElasticNet

from src.Datascience_proj.config.configuration import ModelTrainerConfig
import joblib
from src.Datascience_proj.utils.common import save_bin
import os
from pathlib import Path
from typing import Any

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config= config

    def train_model(self):
        
        ## importing the training and test dataset
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        ## splitting independent and target features
        #train
        train_X = train_data.drop([self.config.TARGET_COLUMN], axis=1)
        train_y = train_data[[self.config.TARGET_COLUMN]]

        #test
        test_X = test_data.drop([self.config.TARGET_COLUMN],axis=1)
        test_y = test_data[[self.config.TARGET_COLUMN]]

        ## initializing ml model
        lr = ElasticNet(alpha = self.config.alpha, l1_ratio= self.config.l1_ratio, 
                        random_state = self.config.random_state)

        ## training the model
        lr.fit(train_X, train_y)
        

        ## saving the model
        joblib.dump(lr, os.path.join(self.config.rootdir, self.config.model_name))
        #save_bin(Any(lr), Path(os.path.join(self.config.rootdir, self.config.model_name)))
