from collections.abc import Sequence


class Remix(Sequence):
    """Remix represents a sequence of beats."""

    def __init__(self, *beats):
        self._beats = list(beats)

    def __len__(self):
        return len(self._beats)

    def __getitem__(self, item):
        return self._beats.__getitem__(item)

    @property
    def last_beat(self):
        num_beats_in_remix = len(self._beats)
        return self._beats[num_beats_in_remix-1]

    @property
    def num_beats_with_last_track(self):
        if len(self._beats) == 1:
            return 1
        num_beats_with_last_track = 0
        previous_beat_track = self.last_beat.track
        for i, beat in enumerate(reversed(self._beats)):
            num_beats_with_last_track += 1
            if beat.track != previous_beat_track:
                return num_beats_with_last_track
            previous_beat_track = beat.track
            if i == len(self) - 1:
                return num_beats_with_last_track

    @property
    def file_paths(self):
        file_paths = [beat.file_path for beat in self._beats]
        return file_paths

    def append(self, beat):
        self._beats.append(beat)

    def reset(self):
        self._beats = []