import numpy as np

from infiniteremixer.data.aggregation.aggregator import Aggregator


class MeanAggregator(Aggregator):
    """MeanAggregator is responsible for aggregating a array using mean
    across a specified axis.
    """

    def __init__(self, aggregation_axis):
        super().__init__("mean")
        self.aggregation_axis = aggregation_axis

    def aggregate(self, array):
        """Aggregate array using mean across 1 axis

        :param array: (np.ndarray)

        :return: (np.ndarray) Aggregated array
        """
        return np.mean(array, axis=self.aggregation_axis)