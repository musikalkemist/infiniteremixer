from infiniteremixer.data.aggregation.batchaggragator import BatchAggregator
from infiniteremixer.utils.array_manipulation import concatenate_arrays


class FlatBatchAggregator(BatchAggregator):
    """FlatBatchAggregator is a concrete BatchAggregator that applies multiple
    statistical aggregation on 2d numpy arrays and merges them into a single
    array.
    """

    def aggregate(self, array):
        """Perform statistical aggregations on 2d array and merge
        aggregations.

        :param array: (2d numpy array)

        :return (np.ndarray) Aggregated and merged values
        """
        merged_aggregations = []
        for aggregator in self.aggregators:
            aggregation = aggregator.aggregate(array)
            merged_aggregations.append(aggregation)
        return concatenate_arrays(merged_aggregations)