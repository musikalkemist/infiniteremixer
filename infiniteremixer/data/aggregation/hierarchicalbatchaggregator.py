from infiniteremixer.data.aggregation.batchaggragator import BatchAggregator


class HierarchicalBatchAggregator(BatchAggregator):
    """HierarchicalBatchAggregator is a concrete BatchAggregator that applies
    multiple statistical aggregation on 2d numpy arrays and keeps track of
    each.
    """

    def aggregate(self, array):
        """Perform statistical aggregations on 2d array.

        :param array: (2d numpy array)

        :return Dictionary with aggregated values of the form:
            {
                "aggregation_type1": np.array([1, 2, 3]),
                "aggregation_type2": np.array([1, 2, 3]),
                ...
            }
        """
        aggregations = {}
        for aggregator in self.aggregators:
            aggregations[aggregator.name] = aggregator.aggregate(array)
        return aggregations