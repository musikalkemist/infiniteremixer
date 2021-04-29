import random
import math

from infiniteremixer.remix.beat import Beat


class BeatSelector:
    """BeatSelector is responsible for selecting a beat for a remix"""

    def __init__(self, jump_rate):
        self.jump_rate = jump_rate
        self.nn_search = None
        self.feature_retriever = None
        self.beat_file_paths = None

    def choose_beat(self, remix):
        """Select next beat in the remix.

        :param remix: (Remix) Remix

        :return: (Beat) New selected beat
        """
        if len(remix) == 0:
            return self._choose_first_beat()
        if self._is_beat_jump(remix.num_beats_with_last_track):
            return self._choose_beat_with_jump(remix.last_beat)
        return self._get_next_beat_in_track_if_possible_or_random(remix.last_beat)

    def _choose_first_beat(self):
        return self._choose_beat_randomly()

    def _choose_beat_randomly(self):
        chosen_beat_file_path = random.choice(self.beat_file_paths)
        return Beat.from_file_path(chosen_beat_file_path)

    def _is_beat_jump(self, num_beats_with_last_track):
        threshold = self._calculate_jump_threshold(num_beats_with_last_track)
        if random.random() <= threshold:
            return True
        return False

    def _calculate_jump_threshold(self, num_beats_with_last_track):
        if num_beats_with_last_track > 0:
            return self.jump_rate * math.log(num_beats_with_last_track, 10)
        return 0

    def _choose_beat_with_jump(self, last_beat):
        feature_vector = self.feature_retriever.get_feature_vector(last_beat.file_path)
        next_beat_file_paths, _ = self.nn_search.get_closest(feature_vector,
                                                             500)
        next_beat = self._get_closest_beat_of_different_track(next_beat_file_paths, last_beat)
        return next_beat

    def _get_closest_beat_of_different_track(self, beat_file_paths, last_beat):
        for file_path in beat_file_paths:
            beat = Beat.from_file_path(file_path)
            if beat.track != last_beat.track:
                return beat
        return Beat.from_file_path(beat_file_paths[0])

    def _get_next_beat_in_track_if_possible_or_random(self, beat):
        next_number = beat.number + 1
        next_beat_file_path = Beat.replace_number_in_file_path(beat.file_path,
                                                               next_number)
        if next_beat_file_path in self.beat_file_paths:
            return Beat.from_file_path(next_beat_file_path)
        return self._choose_beat_randomly()