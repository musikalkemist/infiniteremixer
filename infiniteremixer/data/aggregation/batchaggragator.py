from abc import abstractmethod, ABC


class BatchAggregator(ABC):
    """BatchAggregator is an abstract class that provides an interface
    to apply multiple statistical aggregation on 2d numpy arrays.
    """

    def __init__(self):
        self.aggregators = []

    def add_aggregator(self, aggregator):
        """Add an aggregator function to the aggregators.

        :param aggregator: (Aggregator) Concrete Aggregator
        """
        self.aggregators.append(aggregator)

    @abstractmethod
    def aggregate(self, array):
        pass