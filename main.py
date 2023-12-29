from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainPipeline
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainPipeline
from textSummarizer.pipeline.stage_04_model_trainer import ModelTrainerTrainPipeline
from textSummarizer.pipeline.stage_05_model_evaluation import ModelEvaluationTrainPipeline
from textSummarizer.logging import logger

STAGE_NAME = "Data_Ingestion_stage"
try:
    logger.info ( f">>>>> stage {STAGE_NAME} started <<<<<" )
    data_ingestion = DataIngestionTrainPipeline()
    data_ingestion.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation stage"
try:
    logger.info ( f">>>>> stage {STAGE_NAME} started <<<<<" )
    data_validation = DataValidationTrainPipeline()
    data_validation.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation stage"
try:
    logger.info ( f">>>>> stage {STAGE_NAME} started <<<<<" )
    data_transformation = DataTransformationTrainPipeline()
    data_transformation.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Trainer stage"
try:
    logger.info ( f">>>>> stage {STAGE_NAME} started <<<<<" )
    model_trainer = ModelTrainerTrainPipeline()
    model_trainer.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Evaluation stage"
try:
    logger.info ( f">>>>> stage {STAGE_NAME} started <<<<<" )
    model_evaluation = ModelEvaluationTrainPipeline()
    model_evaluation.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e

