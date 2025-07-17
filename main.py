from src.Datascience_proj import logger
from src.Datascience_proj.pipeline.data_ingestion_pipeline import DataIngestiontrainingPipeline
from src.Datascience_proj.pipeline.data_validation_pipeline import DataValidationtrainingPipeline
from src.Datascience_proj.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.Datascience_proj.pipeline.model_training_pipeline import ModelTrainerPipeline
from src.Datascience_proj.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline


STAGE_NAME= "Data Ingestion Stage"
try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
        data_ingestion = DataIngestiontrainingPipeline()
        data_ingestion.initiate_data_ingestion()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx=========================================x")
    
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME= "Data Validation Stage"
try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
        data_validation = DataValidationtrainingPipeline()
        data_validation.initiate_data_validation()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx=========================================x")
    
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME= 'Data Transformation Stage'
try:
        logger.info(f">>>>>>> {STAGE_NAME} Started! <<<<<<<")
        transform_pipeline = DataTransformationPipeline()
        transform_pipeline.initiate_data_transformation()
        logger.info(f">>>>>>> {STAGE_NAME} Completed! <<<<<<<\n\nx==============================================x")

except Exception as e:
        raise e


STAGE_NAME= "Model Trainer Stage"

     
try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
        model_trainer = ModelTrainerPipeline()
        model_trainer.model_trainer()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx=========================================x")

except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Model Evaluation Stage"


try:
        logger.info(f">>>>>>> {STAGE_NAME} Started! <<<<<<<")
        evaluation_pipeline = ModelEvaluationPipeline()
        evaluation_pipeline.initiate_model_evaluation()
        logger.info(f">>>>>>> {STAGE_NAME} Completed! <<<<<<<\n\n==============================================")

except Exception as e:
        raise e
