import pytest
import numpy as np

from infiniteremixer.data.aggregation.flatbatchaggregator import FlatBatchAggregator
from infiniteremixer.data.aggregation.meanaggregator import MeanAggregator
from infiniteremixer.data.aggregation.stdevaggregator import StdDeviationAggregator


@pytest.fixture
def flat_batch_aggregator():
    mean_aggregator = MeanAggregator(1)
    std_aggregator = StdDeviationAggregator(1)

    ba = FlatBatchAggregator()

    ba.add_aggregator(mean_aggregator)
    ba.add_aggregator(std_aggregator)
    return ba


def test_flat_batch_aggregator_is_instantiated(flat_batch_aggregator):
    assert isinstance(flat_batch_aggregator, FlatBatchAggregator)


def test_array_is_aggregated(flat_batch_aggregator):
    array = np.array([
        [1, 2],
        [3, 4]
    ])
    aggregations = flat_batch_aggregator.aggregate(array)
    expected_aggregations = np.array([1.5, 3.5, .5, .5])
    assert np.array_equal(aggregations, expected_aggregations)