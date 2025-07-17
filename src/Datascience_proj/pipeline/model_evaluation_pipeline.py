from src.Datascience_proj.config.configuration import ConfigurationManager
from src.Datascience_proj.components.model_evaluation import ModelEvaluation
from src.Datascience_proj import logger
from pathlib import Path

STAGE_NAME = "Model Evaluation Stage"
class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation = ModelEvaluation(config=model_evaluation_config)
            model_evaluation.log_into_mlflow()

        except Exception as e:
            raise e

    

if __name__=="__main__()":
    try:
        logger.info(f">>>>>>> {STAGE_NAME} Started! <<<<<<<")
        evaluation_pipeline = ModelEvaluationPipeline()
        evaluation_pipeline.initiate_model_evaluation()
        logger.info(f">>>>>>> {STAGE_NAME} Completed! <<<<<<<\n\n==============================================")

    except Exception as e:
        raise e
