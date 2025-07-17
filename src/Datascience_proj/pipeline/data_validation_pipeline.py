from src.Datascience_proj.config.configuration import ConfigurationManager
from src.Datascience_proj.components.data_validation import DataValidation
from src.Datascience_proj import logger


STAGE_NAME = "Data Validation Stage"

class DataValidationtrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_validation(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config= data_validation_config)
        data_validation.validate_all_columns()




STAGE_NAME= "Data Validation Stage"

if __name__== '__main__()':
     
    try:
            logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
            data_validation = DataValidationtrainingPipeline()
            data_validation.initiate_data_validation()
            logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx=========================================x")
        
    except Exception as e:
        logger.exception(e)
        raise e

