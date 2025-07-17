from src.Datascience_proj.config.configuration import ConfigurationManager
from src.Datascience_proj.components.model_trainer import ModelTrainer
from src.Datascience_proj import logger


STAGE_NAME = "Model Trainer Stage"

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def model_trainer(self):
        config= ConfigurationManager()
        config_model = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config_model)
        model_trainer.train_model()


STAGE_NAME= "Model Trainer Stage"

if __name__== '__main__()':
     
    try:
            logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
            model_trainer = ModelTrainerPipeline()
            model_trainer.model_trainer()
            logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx=========================================x")
        
    except Exception as e:
        logger.exception(e)
        raise e

