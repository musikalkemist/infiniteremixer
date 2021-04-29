import numpy as np


class DataPreparer:
    """DataPreparer is responsible to prepare the dataset that will be used
    by KNN, and a mapping of dataset indexes / file paths, that will be
    necessary for retrieval."""

    def __init__(self):
        pass

    def prepare_mapping_and_dataset(self, features):
        """Create mapping and dataset from tracks with relative features.

        :param features: (dict) Tracks with features:
            {
                "filepath1": np.ndarray([ 1, 2, ...]),
                "filepath2": np.ndarray([1, 2, ...])
            }

        :return: (list) Mapping of file paths with indexes in the dataset:
            ["filepath1", "filepath2"]
        :return: (np.ndarray) Array dataset with features for each track
        """
        mapping = self._prepare_mapping(features)
        dataset = self._prepare_dataset(features)
        return mapping, dataset

    def _prepare_mapping(self, features):
        return list(features.keys())

    def _prepare_dataset(self, features):
        dataset = list(features.values())
        dataset = np.asarray(dataset)
        return dataset