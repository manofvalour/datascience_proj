from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir:Path
    source_url:str
    local_data_file:Path
    unzip_dir:Path

@dataclass
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE:str
    unzip_data_dir: Path
    all_schema: dict

@dataclass
class DataTransformationConfig:
    root_dir: Path
    unzip_data_dir: Path
    TRAIN_DATA: str
    TEST_DATA: str
    params: dict

@dataclass
class ModelTrainerConfig:
    rootdir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: Path
    alpha: float
    l1_ratio: float
    random_state: int
    TARGET_COLUMN:str


@dataclass
class ModelEvaluationConfig:
    root_dir: Path
    test_data_path: Path
    model_path: Path
    all_params: dict
    metric_filename: Path
    TARGET_COLUMN: str
    #mlflow_uri: str