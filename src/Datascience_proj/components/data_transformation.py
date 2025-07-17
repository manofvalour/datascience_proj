from src.Datascience_proj import logger
from src.Datascience_proj.config.configuration import DataTransformationConfig

from sklearn.model_selection import train_test_split
import pandas as pd

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config= config

    ## Note: you can add different data transformation techniques such as scaler, PCA, and all
    ##You can perform all kinds of EDA in ML Cycle here before passing data to the model

    # I am only adding train_test_splitting cos this data is already cleaned up

    def train_test_split(self):

        ## importing the dataset as a dataframe
        data = pd.read_csv(self.config.unzip_data_dir)

        ## splitting the dataset using train test split
        train_data, test_data = train_test_split(data, test_size=self.config.params.test_ratio, 
                                                 random_state=self.config.params.random_state)
        
        ## saving the splitted files
        train_data.to_csv(self.config.TRAIN_DATA, index= False)
        test_data.to_csv(self.config.TEST_DATA, index=False)

        logger.info('Splitted data into training and test datasets')
        logger.info(f"Training Data: {train_data.shape}")
        logger.info(f"Test Data: {test_data.shape}")

        print(f"Training Data: {train_data.shape}")
        print(f"Test Data: {test_data.shape}")