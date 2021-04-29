import os

from infiniteremixer.utils.io import load


class BatchExtractor:
    """Batch extract features dynamically from a list of audio files."""

    def __init__(self, sample_rate=22050):
        self.sample_rate = sample_rate
        self.extractors = []
        self._features = {}

    def add_extractor(self, extractor):
        """Add a concrete Extractor to the extractors.

        :param extractor: (Extractor) Concrete Extractor (e.g., MFCCExtractor)
        """
        self.extractors.append(extractor)

    def extract(self, dir):
        """Extract features from all the audio files in the directory.

        :param dir: (str) Path to directory with audio files to analyse

        :return: (dict): Dictionary with audio file paths as keys and
            extracted features in the form:
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
        """
        features = {}
        for root, _, files in os.walk(dir):
            for file in files:
                file_path = os.path.join(root, file)
                file_features = self._extract_features_for_file(file_path)
                features[file_path] = file_features
        return features

    def _extract_features_for_file(self, file_path):
        features = {}
        signal = load(file_path, self.sample_rate)
        for extractor in self.extractors:
            feature = extractor.extract(signal, self.sample_rate)
            features[extractor.feature_name] = feature
        return features


if __name__ == "__main__":
    from infiniteremixer.data.extraction.mfccextractor import MFCCExtractor
    from infiniteremixer.data.extraction.chromogramextractor import ChromogramExtractor

    num_mfccs = 13
    frame_size = 1024
    hop_size = 512

    dir = "/home/valerio/datasets/infinitemixer/beats"

    mfcc_extractor = MFCCExtractor(frame_size, hop_size, num_mfccs)
    chromogram_extractor = ChromogramExtractor(frame_size, hop_size)

    batch_extractor = BatchExtractor(22050)
    batch_extractor.add_extractor(mfcc_extractor)
    batch_extractor.add_extractor(chromogram_extractor)

    features = batch_extractor.extract(dir)
    a = 1


