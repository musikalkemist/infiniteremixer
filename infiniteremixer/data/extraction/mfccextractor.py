import librosa

from infiniteremixer.data.extraction.extractor import Extractor


class MFCCExtractor(Extractor):
    """Concrete Extractor that extracts MFCC sequences from signal."""

    def __init__(self, frame_size=1024, hop_length=512, num_coefficients=13):
        super().__init__("mfcc")
        self.frame_size = frame_size
        self.hop_length = hop_length
        self.num_coefficients = num_coefficients

    def extract(self, signal, sample_rate):
        """Extract MFCC from time series using librosa.

        :param signal: (np.ndarray) Audio time series
        :param sr: (int) Sample rate

        :return: (np.ndarray) MFCC sequence
        """
        mfcc = librosa.feature.mfcc(signal,
                                    n_mfcc=self.num_coefficients,
                                    n_fft=self.frame_size,
                                    hop_length=self.hop_length,
                                    sr=sample_rate)
        return mfcc