import pytest
import numpy as np

from infiniteremixer.data.aggregation.multitrackbatchaggregator import MultiTrackBatchAggregator
from infiniteremixer.data.aggregation.hierarchicalbatchaggregator import HierarchicalBatchAggregator
from infiniteremixer.data.aggregation.meanaggregator import MeanAggregator
from infiniteremixer.data.aggregation.stdevaggregator import StdDeviationAggregator


@pytest.fixture
def mtba():
    ba = HierarchicalBatchAggregator()
    mean_aggregator = MeanAggregator(0)
    std_aggregator = StdDeviationAggregator(0)
    ba.add_aggregator(mean_aggregator)
    ba.add_aggregator(std_aggregator)

    mtba = MultiTrackBatchAggregator()
    mtba.batch_aggregator = ba
    return mtba


def test_mtba_is_instantiated_correctly(mtba):
    assert isinstance(mtba, MultiTrackBatchAggregator)


def test_mtba_generate_tracks_aggregations(mtba):
    tracks_features = {
        "filepath1": {
            "chromogram": np.array([[1, 3], [2, 6]]),
            "mfcc": np.array([[2, 4], [1, 2]])
        },
        "filepath2": {
            "chromogram": np.array([[1, 3], [2, 6]]),
            "mfcc": np.array([[2, 4], [1, 2]])
        },
    }

    aggregations = mtba.aggregate(tracks_features)

    expected_aggregations = {
        "filepath1": {
            "chromogram": {
                "mean": np.array([1.5, 4.5]),
                "std_deviation": np.array([0.5, 1.5]),
            },
            "mfcc": {
                "mean": np.array([1.5, 3]),
                "std_deviation": np.array([.5, 1]),
            },
        },
        "filepath2": {
            "chromogram": {
                "mean": np.array([1.5, 4.5]),
                "std_deviation": np.array([0.5, 1.5]),
            },
            "mfcc": {
                "mean": np.array([1.5, 3]),
                "std_deviation": np.array([.5, 1]),
            },
        }
    }
    assert len(aggregations) == len(expected_aggregations)
    assert np.array_equal(aggregations["filepath1"]["chromogram"]["mean"],
                          expected_aggregations["filepath1"]["chromogram"]["mean"])
    assert np.array_equal(aggregations["filepath1"]["chromogram"]["std_deviation"],
                          expected_aggregations["filepath1"]["chromogram"]["std_deviation"])
    assert np.array_equal(aggregations["filepath1"]["mfcc"]["mean"],
                          expected_aggregations["filepath1"]["mfcc"]["mean"])
    assert np.array_equal(aggregations["filepath1"]["mfcc"]["std_deviation"],
                          expected_aggregations["filepath1"]["mfcc"]["std_deviation"])