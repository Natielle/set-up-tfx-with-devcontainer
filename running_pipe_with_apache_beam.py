from absl import logging
import os
import tensorflow as tf
import tfx
from tfx.utils.dsl_utils import csv_input, external_input
from tfx.orchestration import pipeline
from tfx.components import StatisticsGen, SchemaGen
from tfx.components.example_gen.csv_example_gen.component import CsvExampleGen
from tfx.orchestration.beam.beam_dag_runner import BeamDagRunner
from tfx.orchestration import metadata


if __name__ == '__main__':
  logging.set_verbosity(logging.INFO)
  logging.info('TensorFlow version: {}'.format(tf.__version__))
  logging.info('TFX version: {}'.format(tfx.__version__))

  PIPELINE_NAME = 'my_pipeline'
  PIPELINE_ROOT = os.path.join('.', 'my_pipeline_output')
  METADATA_PATH = os.path.join('.', 'tfx_metadata', 'metadata.db')
  DATA_DIR = "/app/data/"
  components = []

  logging.info("Creating component to read csv")
  data_path = external_input(os.path.join(DATA_DIR))
  example_gen = CsvExampleGen(data_path) 
  logging.info("Component was created")

  statistics_gen = StatisticsGen(examples=example_gen.outputs['examples'])
  schema_gen = SchemaGen(statistics=statistics_gen.outputs['statistics'], infer_feature_shape=False)
 
  components.append(example_gen)
  components.append(statistics_gen)
  components.append(schema_gen)

  logging.info("Creating pipeline")
  pipe = pipeline.Pipeline(
    pipeline_name=PIPELINE_NAME,
    pipeline_root=PIPELINE_ROOT,
    metadata_connection_config=metadata.sqlite_metadata_connection_config(METADATA_PATH),
    components=components,
    enable_cache=True,
  )
  logging.info("Running pipeline")
  BeamDagRunner().run(pipe)
  logging.info("Pipeline finished")


  logging.info("Showing example_gen outputs")
  logging.info(example_gen.outputs['examples'])
  # artifact = example_gen.outputs['examples'].get()[0]
  # logging.info("details: ", artifact)
  # logging.info("URI: ", artifact.uri)

  logging.info("Showing stats_gen")
  # logging.info(statistics_gen.outputs['statistics'])

  logging.info("Showing schema gen")
  # logging.info(schema_gen.outputs['schema'])
  logging.info("Finished")

