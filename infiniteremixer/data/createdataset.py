import argparse

from infiniteremixer.data.datasetpipeline import DatasetPipeline
from infiniteremixer.data.extraction.batchextractor import BatchExtractor
from infiniteremixer.data.extraction.chromogramextractor import ChromogramExtractor
from infiniteremixer.data.extraction.mfccextractor import MFCCExtractor
from infiniteremixer.data.aggregation.flatbatchaggregator import FlatBatchAggregator
from infiniteremixer.data.aggregation.meanaggregator import MeanAggregator
from infiniteremixer.data.aggregation.multitrackbatchaggregator import MultiTrackBatchAggregator
from infiniteremixer.data.featuremerger import FeatureMerger
from infiniteremixer.data.datapreparer import DataPreparer


def create_dataset():
    """The "create_embeddings" entry point can be run to generate a dataset
    from audio files in a directory. Features will be extracted, aggregated
    and stored. Along with features a mapping of indexes / file paths will
    also be stored.

    To run the script type:

    $ create_dataset path/to/dir/with/audio/files save/dir
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("dir",
                        help="directory with audio files to create "
                             "embeddings for")
    parser.add_argument("save_dir",
                        help="directory where to store generated dataset and "
                             "mapping")
    args = parser.parse_args()
    data_pipeline = _create_data_pipeline()
    data_pipeline.process(args.dir, args.save_dir)


def _create_data_pipeline():
    """Generate a data pipeline object. This is a quick and dirty function,
    which should be converted into a data pipeline builder class. This class
    would enable a client to create data pipeline objects dinamically,
    for example, choosing different aggregators and extractors."""

    batch_extractor = BatchExtractor()
    chromogram_extractor = ChromogramExtractor()
    batch_extractor.add_extractor(chromogram_extractor)
    mfcc_extractor = MFCCExtractor()
    batch_extractor.add_extractor(mfcc_extractor)

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
