import librosa

from infiniteremixer.data.extraction.extractor import Extractor


class ChromogramExtractor(Extractor):
    """Concrete Extractor that extracts chromogram from signal."""

    def __init__(self, frame_size=1024, hop_length=512):
        super().__init__("chromogram")
        self.frame_size = frame_size
        self.hop_length = hop_length

    def extract(self, signal, sample_rate):
        """Extract chromogram from time series using librosa.

        :param signal: (np.ndarray) Audio time series
        :param sr: (int) Sample rate

        :return: (np.ndarray) Chromogram
        """
        chromogram = librosa.feature.chroma_stft(signal,
                                                 n_fft=self.frame_size,
                                                 hop_length=self.hop_length,
                                                 sr=sample_rate)
        return chromogram