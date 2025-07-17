from src.Datascience_proj.config.configuration import ConfigurationManager
from src.Datascience_proj.components.data_transformation import DataTransformation
from src.Datascience_proj import logger
from pathlib import Path

STAGE_NAME = "Data Transformation Stage"
class DataTransformationPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"),'r') as f:
                status = f.read().split(" ")[-1]
            if status== "True":
                        
                config = ConfigurationManager()
                data_transformation_config=config.get_data_transformation_config()
                transform_data= DataTransformation(data_transformation_config)
                transform_data.train_test_split()
            else:
                raise Exception("Your Data schema is not valid")
                
        except Exception as e:
            print(e)

    

if __name__=="__main__()":
    try:
        logger.info(f">>>>>>> {STAGE_NAME} Started! <<<<<<<")
        transform_pipeline = DataTransformationPipeline()
        transform_pipeline.initiate_data_transformation()
        logger.info(f">>>>>>> {STAGE_NAME} Completed! <<<<<<<\n\n==============================================")

    except Exception as e:
        raise e