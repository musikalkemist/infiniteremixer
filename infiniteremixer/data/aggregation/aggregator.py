from abc import ABC, abstractmethod


class Aggregator(ABC):
    """Interface for a concrete statistical aggregator."""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def aggregate(self, array):
        pass

