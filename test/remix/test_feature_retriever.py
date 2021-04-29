import pytest
import numpy as np

from infiniteremixer.remix.featureretriever import FeatureRetriever


@pytest.fixture
def feature_retriever():
    feature_retriever = FeatureRetriever()
    feature_retriever.mapping = [
        "beat1",
        "beat2",
        "beat3"
    ]
    feature_retriever.features = np.array([
        [1, 2],
        [2, 3],
        [3, 4]
    ])
    return feature_retriever


def test_feature_retriever_is_instantiated(feature_retriever):
    assert isinstance(feature_retriever, FeatureRetriever)


def test_feature_vector_is_returned(feature_retriever):
    feature_vector = feature_retriever.get_feature_vector("beat1")
    expected_feature_vector = np.array([1, 2])
    assert np.array_equal(feature_vector, expected_feature_vector)