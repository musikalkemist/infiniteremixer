import pytest
import numpy as np

from infiniteremixer.data.datapreparer import DataPreparer


@pytest.fixture
def data_preparer():
    return DataPreparer()


def test_data_preparer_is_instantiated_correctly():
    data_preparer = DataPreparer()
    assert isinstance(data_preparer, DataPreparer)


def test_mapping_and_dataset_are_returned(data_preparer):
    features = {
        "track1": np.array([1, 2, 3]),
        "track2": np.array([3, 4, 5]),
    }
    mapping, dataset = data_preparer.prepare_mapping_and_dataset(features)
    expected_dataset = np.array([
        [1, 2, 3],
        [3, 4, 5]
    ])
    assert mapping == ["track1", "track2"]
    assert np.array_equal(dataset, expected_dataset)