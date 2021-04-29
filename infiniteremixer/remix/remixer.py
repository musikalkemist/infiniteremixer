from infiniteremixer.remix.remix import Remix


class Remixer:
    """Remixer is responsible to generate a remix made up of multiple beats."""

    def __init__(self, number_of_beats):
        self.number_of_beats = number_of_beats
        self.beat_selector = None

    def generate_remix(self):
        """Generate a remix.

        :return: (Remix) Generated remix
        """
        remix = Remix()
        for _ in range(self.number_of_beats):
            beat = self._choose_beat(remix)
            remix.append(beat)
        return remix

    def _choose_beat(self, remix):
        return self.beat_selector.choose_beat(remix)