from abc import ABC, abstractmethod


class Extractor(ABC):
    """Interface for feature extractors."""

    def __init__(self, feature_name):
        self.feature_name = feature_name

    @abstractmethod
    def extract(self, signal, sample_rate):
        pass
