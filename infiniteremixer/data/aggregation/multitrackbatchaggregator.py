class MultiTrackBatchAggregator:
    """MultiTrackBatchAggregator aggregates features which characterise a
    set of tracks.
    """

    def __init__(self):
        self.batch_aggregator = None

    def aggregate(self, tracks_features):
        """Substitute features for each track with respective aggregations.

        :param tracks_features: (dict) Tracks with corresponding features:
            {
                "filepath1": {
                    "chromogram": np.ndarray([[], [], ...]),
                    "mfcc": np.ndarray([[], [], ...])
                },
                "filepath2": {
                    "chromogram": np.ndarray([[], [], ...]),
                    "mfcc": np.ndarray([[], [], ...])
                },
                ...
            }

        :return: tracks_aggregations: (dict) Tracks with aggregated features
            {
                "filepath1": {
                    "chromogram": {
                        "mean": np.ndarray([[], [], ...]),
                        "standard_deviation": np.ndarray([[], [], ...]),
                    }
                    "mfcc": {
                        "mean": np.ndarray([[], [], ...]),
                        "standard_deviation": np.ndarray([[], [], ...]),
                    }
                },
                "filepath1": {
                    "chromogram": {
                        "mean": np.ndarray([[], [], ...]),
                        "standard_deviation": np.ndarray([[], [], ...]),
                    }
                    "mfcc": {
                        "mean": np.ndarray([[], [], ...]),
                        "standard_deviation": np.ndarray([[], [], ...]),
                    }
                },
                ...
            }
        """
        tracks_aggregations = {}
        for track_path, track_features in tracks_features.items():
            features_aggregations = {}
            for feature_type, features in track_features.items():
                aggregations = self.batch_aggregator.aggregate(features)
                features_aggregations[feature_type] = aggregations
            tracks_aggregations[track_path] = features_aggregations
        return tracks_aggregations
