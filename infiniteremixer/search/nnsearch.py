import numpy as np


class NNSearch:
    """NNSearch is responsible to get the closest samples to a
    reference samples, using nearest neighbour.
    """

    def __init__(self):
        self.model = None
        self.mapping = None

    def get_closest(self, sample, num_neighbours=1):
        """Returns the file paths of the neighbours of a sample

        :param sample: (array) Sample of which we want to find the neighbours
        :param num_neighbours: (int) # of neighbours to return

        :return: (list of str) Paths associated to the indexes of the
            neighbours
        :return: (np.ndarray) Distances associated to neighbours
        """
        sample = sample[np.newaxis, ...]
        distances, array_indexes = self.model.kneighbors(sample,
                                                         n_neighbors=num_neighbours)
        paths = self._from_indexes_to_paths(array_indexes[0])
        return paths, distances[0]

    def _from_indexes_to_paths(self, sample_indexes):
        paths = [self.mapping[x] for x in sample_indexes]
        return paths