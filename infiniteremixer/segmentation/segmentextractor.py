import os

from infiniteremixer.utils.io import load, write_wav
from infiniteremixer.segmentation.beattracker import estimate_beats
from infiniteremixer.segmentation.trackcutter import cut


class SegmentExtractor:
    """SegmentExtractor is responsible to divide songs into beats and save
    the corresponding signals as audio files.
    """

    def __init__(self, sample_rate):
        self.sample_rate = sample_rate
        self._audio_format = "wav"

    def create_and_save_segments(self, dir, save_dir):
        """Performs the following steps for each audio file in a
        directory:
            1- load audio file
            2- extract beat locations
            3- segment signal into as many chunks as beats we have
            4- save audio segments to wav

        :param dir: (str) Directory containing audio files to be preprocessed
        :param save_dir: (str) Directory where to save segments
        """
        for root, _, files in os.walk(dir):
            for file in files:
                self._create_and_save_segments_for_file(file, dir, save_dir)

    def _create_and_save_segments_for_file(self, file, root, save_dir):
        file_path = os.path.join(root, file)
        signal = load(file_path, self.sample_rate)
        beat_events = estimate_beats(signal, self.sample_rate)
        segments = cut(signal, beat_events)
        self._write_segments_to_wav(file, save_dir, segments)
        print(f"Beats saved for {file_path}")

    def _write_segments_to_wav(self, file, save_dir, segments):
        for i, segment in enumerate(segments):
            save_path = self._generate_save_path(file, save_dir, i)
            write_wav(save_path, segment, self.sample_rate)

    def _generate_save_path(self, file, save_dir, num_segment):
        file_name = f"{file}_{num_segment}.{self._audio_format}"
        save_path = os.path.join(save_dir, file_name)
        return save_path


