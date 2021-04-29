class FeatureRetriever:
    """FeatureRetriever is responsible for retrieving feature vectors for
    beats.
    """

    def __init__(self):
        self.mapping = None
        self.features = None

    def get_feature_vector(self, file_path):
        """Get the feature vector associated to a file path.

        :param file_path: (str) File path of beat to retrieve feature vector for

        :return: (np.ndarray) Feature vector associated to beat
        """
        array_index = self._from_path_to_index(file_path)
        feature_vector = self.features[array_index]
        return feature_vector

    def _from_path_to_index(self, file_path):
        return self.mapping.index(file_path)
