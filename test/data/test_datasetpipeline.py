import os
import pickle

import pytest

from infiniteremixer.data.datasetpipeline import DatasetPipeline
from infiniteremixer.data.extraction.batchextractor import BatchExtractor
from infiniteremixer.data.extraction.chromogramextractor import ChromogramExtractor
from infiniteremixer.data.aggregation.flatbatchaggregator import FlatBatchAggregator
from infiniteremixer.data.aggregation.meanaggregator import MeanAggregator
from infiniteremixer.data.aggregation.multitrackbatchaggregator import MultiTrackBatchAggregator
from infiniteremixer.data.featuremerger import FeatureMerger
from infiniteremixer.data.datapreparer import DataPreparer


@pytest.fixture
def dataset_pipeline():
    batch_extractor = BatchExtractor()
    chromogram_extractor = ChromogramExtractor()
    batch_extractor.add_extractor(chromogram_extractor)

    batch_aggregator = FlatBatchAggregator()
    mean_aggregator = MeanAggregator(1)
    batch_aggregator.add_aggregator(mean_aggregator)

    mtba = MultiTrackBatchAggregator()
    mtba.batch_aggregator = batch_aggregator

    feature_merger = FeatureMerger()
    data_preparer = DataPreparer()

    dataset_pipeline = DatasetPipeline()
    dataset_pipeline.batch_extractor = batch_extractor
    dataset_pipeline.multi_track_batch_aggregator = mtba
    dataset_pipeline.feature_merger = feature_merger
    dataset_pipeline.data_preparer = data_preparer

    return dataset_pipeline


def test_dataset_pipeline_is_instantiated(dataset_pipeline):
    assert isinstance(dataset_pipeline, DatasetPipeline)


def test_dataset_and_mapping_are_generated(dataset_pipeline):
    dummy_beats_dir = "/home/valerio/datasets/infiniteremixer/test/dummy_beats"
    save_dir = "/home/valerio/datasets/infiniteremixer/test"
    dataset_pipeline.process(dummy_beats_dir, save_dir)

    mapping_file = os.path.join(save_dir, "mapping.pkl")
    with open(mapping_file, "rb") as f:
        mapping = pickle.load(f)
    expected_mapping = [
        "/home/valerio/datasets/infiniteremixer/test/dummy_beats/pink floyd - another "
        "brick in the wall.mp3_2.wav",
        "/home/valerio/datasets/infiniteremixer/test/dummy_beats/pink floyd - another "
        'brick in the wall.mp3_1.wav',
        "/home/valerio/datasets/infiniteremixer/test/dummy_beats/pink floyd - another "
        "brick in the wall.mp3_3.wav",
        "/home/valerio/datasets/infiniteremixer/test/dummy_beats/pink floyd - another "
        "brick in the wall.mp3_0.wav"
    ]
    assert mapping == expected_mapping

    dataset_file = os.path.join(save_dir, "dataset.pkl")
    with open(dataset_file, "rb") as f:
        dataset = pickle.load(f)
    assert dataset.shape == (4, 12)

    os.remove(mapping_file)
    os.remove(dataset_file)

