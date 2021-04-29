import pickle
import os

import pytest
import numpy as np

from infiniteremixer.search.nnsearch import NNSearch


CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

@pytest.fixture
def nn_selector():
    nns = NNSearch()
    with open(os.path.join(CURRENT_DIR, "mapping.pkl"), "rb") as f:
        mapping = pickle.load(f)
    with open(os.path.join(CURRENT_DIR, "nearestneighbour.pkl"), "rb") as f:
        nn = pickle.load(f)
    nns.mapping = mapping
    nns.model = nn
    return nns


def test_nn_selector_is_instantiated(nn_selector):
    assert isinstance(nn_selector, NNSearch)


def test_nn_selector_selects_correct_number_of_neighbours(nn_selector):
    random_sample = np.random.random(size=(50))
    neighbours, distances = nn_selector.get_closest(random_sample, 2)
    assert len(neighbours) == 2
    assert type(neighbours[0]) == str
    assert len(distances) == 2
