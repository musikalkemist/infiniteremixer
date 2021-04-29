import copy
import os

from infiniteremixer.segmentation.beattracker import estimate_beats
from infiniteremixer.utils.io import load


class BatchBeatTracker:
    """BatchBeatTracker estimates beat event locations for a batch of
    tracks along with global tempo.
    """

    def __init__(self, sample_rate=22050):
        self._track_estimates = {}
        self.sample_rate = sample_rate

    def estimate(self, dir):
        """Estimate beats / tempo for all tracks in a directory.

        :param dir: (str) Directory containing tracks to be analysed
        :return: (dict) Data structure containing info about track path,
            beat events and tempo:
            {
                "track1_path": {
                    "beats": [10, 20 , 30, ...],
                    "tempo": 120
                },
                "track2_path": {
                    "beats": [10, 20 , 30, ...],
                    "tempo": 132
                },
            }
        """
        for root, _, files in os.walk(dir):
            for file in files:
                file_path = os.path.join(root, file)
                estimate = self._estimate_beat_and_tempo_for_file(file_path)
                self._track_estimates[file_path] = estimate
                print(f"Estimated beats and tempo for {file_path}")
        track_estimates = copy.deepcopy(self._track_estimates)
        self._reset_track_estimates()
        return track_estimates

    def _estimate_beat_and_tempo_for_file(self, file_path):
        signal = load(file_path, self.sample_rate)
        beats, tempo = estimate_beats(signal, self.sample_rate)
        estimate = self._prepare_estimate_dict(beats, tempo)
        return estimate

    def _reset_track_estimates(self):
        self._track_estimates = {}

    def _prepare_estimate_dict(self,beats, tempo):
        estimate = {
            "beats": beats,
            "tempo": tempo
        }
        return estimate


if __name__ == "__main__":
    bbt = BatchBeatTracker()
    estimates = bbt.estimate("/home/valerio/datasets/infiniteremixer/songs")
    a = 1

