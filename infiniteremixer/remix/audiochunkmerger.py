import librosa

from infiniteremixer.utils.array_manipulation import concatenate_arrays


class AudioChunkMerger:
    """AudioChunkMerger concatenates audio files together and saves them to a
    single wav file.
    """

    def __init__(self, sample_rate=22050):
        self.sample_rate = sample_rate

    def concatenate(self, audio_file_paths):
        """Concatenate audio files in a single audio file.

        :param audio_file_paths: (list of str) List of audio files to
            concatenate together

        :return: (np.ndarray) Concatenated audio time series
        """
        time_series = [self.load_audio_file(file) for file in audio_file_paths]
        concatenated_time_series = concatenate_arrays(time_series)
        return concatenated_time_series

    def load_audio_file(self, audio_file_path):
        return librosa.load(audio_file_path, sr=self.sample_rate)[0]
