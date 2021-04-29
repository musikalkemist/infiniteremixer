from infiniteremixer.utils.array_manipulation import concatenate_arrays


class FeatureMerger:
    """FeatureMerger is responsible for merging different features which
    characterise a track.
    """
    def merge(self, tracks_features):
        """Merge all features for a list of tracks.

        :param tracks_features: (dict) Tracks with corresponding features:
            {
                "filepath1": {
                    "chromogram": np.ndarray([1, 2, ...]),
                    "mfcc": np.ndarray([1, 2, ...])
                },
                "filepath2": {
                    "chromogram": np.ndarray([1, 2, ...]),
                    "mfcc": np.ndarray([1, 2, ...])
                },
                ...
            }

        :return: (dict) Tracks with merged features:
            {
                "filepath1": np.ndarray([ 1, 2, ...]),
                "filepath2": np.ndarray([1, 2, ...])
            }
        """
        merged_features = {}
        for track_path, track_features in tracks_features.items():
            track_merged_features = self._merge_features_for_track(track_features)
            merged_features[track_path] = track_merged_features
        return merged_features

    def _merge_features_for_track(self, track_features):
        features = [feature for feature in track_features.values()]
        merged_features = concatenate_arrays(features)
        return merged_features


if __name__ == "__main__":
    import numpy as np
    feature_merger = FeatureMerger()
    tracks_features = {
        "track1": {
            "mfcc": np.array([1, 2, 3]),
            "chromogram": np.array([4, 5, 6, 7])
        },
        "track2": {
            "mfcc": np.array([1, 2, 4]),
            "chromogram": np.array([7, 5, 6, 7])
        }
    }
    merged_features = feature_merger.merge(tracks_features)
    a =1