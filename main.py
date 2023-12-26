from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainPipeline
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

